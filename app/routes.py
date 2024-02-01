from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import *
from flask_login import logout_user, login_required, current_user, login_user
from app.models import *
from werkzeug.urls import url_parse
from sqlalchemy.sql import func, insert
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminForm()
    if current_user.username != "Admin":
        return redirect(url_for('home'))
    form.user.choices = [(user.username, user.username) for user in
        User.query.order_by(User.username).all()]
    if request.method == 'POST':
        selectedUser = User.query.filter_by(username=form.user.data).first()
        logList = Logs.query.filter_by(username=form.user.data)
        logCount = 0;
        for l in logList:
            logCount += 1
        t = userLogTable(logList)
        return render_template('admin.html', title='Admin', form=form, table=t
                               ,num=logCount, user=form.user.data)
    return render_template('admin.html', title='Admin', form=form, table='')   

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    currUser = User.query.filter_by(username=current_user.username).first()
    form.fav.choices = [(team.name, team.name) for team in
        Team.query.with_entities(Team.name).distinct(
            Team.name).order_by(Team.name).all()]
    if request.method == 'POST':
        currUser.team_fav = form.fav.data
        flash('Favorite team updated!')
    if currUser.team_fav is None:
        f = 'None'
    else:
        f = currUser.team_fav
        db.session.commit()
    return render_template('profile.html', title='Profile', form=form,
                           user=currUser.username, f=f)

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = QueryForm()
    form.team.choices = [(team.name, team.name) for team in 
        Team.query.with_entities(Team.name).distinct(
            Team.name).order_by(Team.name).all()]
    form.year.choices = [(team.yearID, team.yearID) for team in 
        Team.query.filter_by(name=form.team.data).all()]
    if request.method == 'POST':
        if form.year.data is None:
            return render_template('index.html', title='Team Data', form=form,
                error='Select a year.')
        else:
            selectedTeam = Team.query.filter_by(
                name=form.team.data,yearID=form.year.data).first()
            players = Fielding.query.filter_by(
                teamID=selectedTeam.teamID,yearID=selectedTeam.yearID).all()
            t = playerStatTable(players)
            now = datetime.now()
            l = Logs(username=current_user.username,
                     team_name=form.team.data,
                     yearID=selectedTeam.yearID,
                     time=now)
            db.session.add(l)
            db.session.commit()
            return render_template('index.html', title='Team Data',
                form=form,table=t)

    return render_template('index.html', title='Team Data', form=form, table='')

@app.route('/team/<name>')
def team(name):
    teams = Team.query.filter_by(name=name).all()

    teamNames = []

    for team in teams:
        teamObj = {}
        teamObj['ID'] = team.ID
        teamObj['yearID'] = team.yearID
        teamNames.append(teamObj)

    return jsonify({'teams' : teamNames})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
