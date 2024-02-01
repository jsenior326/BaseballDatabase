# RadRacoons
##### Jake Senior, Ashley Bickham, Nathan Hennigh
RadRacoons in a complete baseball database using data from the Lahman Baseball Database as well as an updated hall of fame data manually added to the already existing file using data found online.
## Setup

Create the database by logging into your DBMS and run the following

```bash
 \. schema.sql
```
Change the username and password in the config file "csi3335sp2022.py" to your login information for your DMBS.
```python
mysql = {
         "host":"localhost",
         "user":"web",
	        "password":'foo',
	        "db":"RadRacoons"
}
```
Load the data by running the following in your terminal in the same directory (This will also load the hall of fame data from load_hall.py. This may take a while).
```bash
python load_data.py
```
Start the Flask app by running the following in your terminal, will run automatically assuming all dependencies have been installed beforehand.
```bash
export FLASK_APP=project.py
flask run
```
The app should now be running on localhost:5000
## Usage
Type in localhost:5000 in your browser. Create an account and navigate to the teams tab. From the teams tab, select a team and year from the drop downs to view information about players' statistics for that season. The admin account with the credentials given below has access to the "Admin" page. On this page the admin can select a user from the dropdown to view logged information about the user.

## Admin Account (must create first, but will be recognized)
```
username = Admin
password = AdminPass
```

## Dependencies
```
pymysql
sqlalchemy
hashlib
sys
datetime
flask
werkzeug
os
flask_login
flask_table
flask_wtf
flask_sqlalchemy
wtforms
```

## File Structure
Installed files should mimic the following file structure.
```
|-- checkStrings.py
|-- load_data.py
|-- load_hall.py
|-- schema.sql
|-- csi3335sp2022.py
|-- config.py
|-- project.py
|-- app
|   |-- __init__.py
|   |-- forms.py
|   |-- routes.py
|   |-- models.py
|   |-- templates
|   |   |-- admin.html
|   |   |-- home.html
|   |   |-- login.html
|   |   |-- register.html
|   |   |-- base.html
|   |   |-- index.html
|   |   |-- profile.html
```

## Extra Data Added
```
Salary
Schools
Strikes (through manually created CSV file)
Awards (Players and Managers)
AwardsShare (Players and Managers)
```
## Errors Fixed
```
Added G_rf in the appearances table
Corrected finalGameDate
Added missing data in fielding table, FieldingOFSplit of added
Replaced wrong data with correct data at ID 5375 in allstarfull
```
## Sources For Extra Data
```
Data for Strikes
https://www.nbcsports.com/washington/nationals/mlb-work-stoppages-history-lockouts-strikes-baseball

Recent Hall of Fame Data
2019
https://www.baseball-reference.com/awards/hof_2019.shtml
2020
https://www.baseball-reference.com/awards/hof_2020.shtml
2021
https://www.baseball-reference.com/awards/hof_2021.shtml
```
