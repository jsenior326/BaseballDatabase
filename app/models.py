from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from flask_table import Table, Col

class User(UserMixin, db.Model):
    id = db.Column(db.Integer)
    username = db.Column(db.String(50),primary_key=True,index=True,unique=True)
    password = db.Column(db.String(200))
    team_fav = db.Column(db.String(50))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return self.username

class Logs(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    team_name = db.Column(db.String(50))
    yearID = db.Column(db.Integer)
    time = db.Column(db.DateTime)

@login.user_loader
def load_user(id):
    return User.query.filter_by(username=id).first()

class Team(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    teamID = db.Column(db.String(3))
    yearID = db.Column(db.Integer)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Team {}>'.format(self.name)

class Fielding(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9))
    yearID = db.Column(db.Integer)
    teamID = db.Column(db.String(3))
    position = db.Column(db.String(2))
    f_G = db.Column(db.Integer)
    f_InnOuts = db.Column(db.Integer)

class playerStatTable(Table):
    playerID = Col('Player')
    f_InnOuts = Col('InnOuts')
    position = Col('Position')
    f_G = Col('Games')
    teamID = Col('Team ID')
    yearID = Col('Year')

class userLogTable(Table):
    username = Col('Username')
    team_name = Col('Team Selected')
    yearID = Col('Year Selected')
    time = Col('Time of Query')
