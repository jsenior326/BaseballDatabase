from operator import attrgetter
from re import S
import sys
import datetime
import csi3335sp2022 as cfg
from checkStrings import *
from sqlalchemy import create_engine, Column, Date, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BaseHall = declarative_base()

class HallOfFame(BaseHall):
    __tablename__ = "HallOfFame"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    votedBy = Column(String(64))
    ballots = Column(Integer)
    needed = Column(Integer)
    votes = Column(Numeric)
    inducted = Column(String(64))
    category = Column(String(64))

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.votedBy = emptyStr(attributes[2])
        self.ballots = emptyInt(attributes[3])
        self.needed = emptyInt(attributes[4])
        self.votes = emptyInt(attributes[5])
        self.inducted = emptyStr(attributes[6])
        self.category = emptyStr(attributes[7])

def initHallOfFame():
    user = cfg.mysql["user"]
    pWord = cfg.mysql["password"]
    host = cfg.mysql["host"]
    db = cfg.mysql["db"]

    # configure session w/ engine
    stringEng = "mysql+pymysql://" + user + ":" + pWord + "@" + host + ":3306/" + db
    eng = create_engine(stringEng)
    Session = sessionmaker(bind=eng)
    session = Session()

    # delete data from table as a test
    session.execute("DELETE FROM  HallOfFame")
    session.commit()

    # begin to read through file
    file = open("./HallOfFame.csv", "r")
    next(file)
    for player in file:
        # put data into the table
        #famer = session.query(HallOfFame).filter_by(playerID = player[1], yearID = player[0])
        #if not famer:
        session.add(HallOfFame(player))

    session.commit()
    session.close()