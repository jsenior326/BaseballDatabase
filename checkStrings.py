import datetime
from math import inf, nan

def emptyDate(year, month, day):
    if year == "":
        return None
    elif day == "" and month == "":
        return datetime.datetime.strptime(year, '%Y')
    elif day == "":
        datestr = year + "-" + month
        return datetime.datetime.strptime(datestr, '%Y-%m')
    else:
        datestr = year + "-" + month + "-" + day
        return datetime.datetime.strptime(datestr, '%y-%m-%d')

def emptyStr(input):
    if input == "" or input == "\n":
        return None
    else:
        return input

def emptyInt(input):
    if input == "" or input == "\n" or input == "inf" or input == "nan":
        return None
    else:
        return int(input)

def emptyFloat(input):
    if input == "" or input == "\n" or input == "inf" or input == "nan":
        return None
    else:
        return float(input)