from ast import In, Str
from code import interact
from lib2to3.pytree import Base
import sys
from tokenize import Double
from unicodedata import name
import pymysql
import csi3335sp2022 as cfg
from checkStrings import *
from load_hall import *
from sqlalchemy import create_engine, Column, Date, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# begin loading tables (alphabetically organized)
BaseAllStar = declarative_base()
BaseAppearances = declarative_base()
BaseAwards = declarative_base()
BaseAwardsShare = declarative_base()
BaseBatting = declarative_base()
BaseBattingPost = declarative_base()
BaseFielding = declarative_base()
BaseFieldingPost = declarative_base()
BaseFranchises = declarative_base()
# HallOfFame located in load_hall
BaseHomeGames = declarative_base()
BaseManagers = declarative_base()
BasePark = declarative_base()
BasePeople = declarative_base()
BasePitching = declarative_base()
BasePitchingPost = declarative_base()
BaseSalary = declarative_base()
BaseSchool = declarative_base()
BaseSeriesPost = declarative_base()
BaseStrikes = declarative_base()
BaseTeam = declarative_base()

# create table classes (alphabetically organized)
class AllStar(BaseAllStar):
    __tablename__ = "AllStarFull"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    gameNum = Column(Integer)
    gameID = Column(String(12))
    teamID = Column(String(3))
    lgID = Column(String(2))
    GP = Column(Integer)
    startingPos = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.gameNum = emptyInt(attributes[2])
        self.gameID = emptyStr(attributes[3])
        self.teamID = emptyStr(attributes[4])
        self.lgID = emptyStr(attributes[5])
        self.GP = emptyInt(attributes[6])
        self.startingPos = emptyInt(attributes[7])

class Appearances(BaseAppearances):
    __tablename__ = "Appearances"
    ID = Column(Integer, primary_key=True)
    yearID = Column(Integer)
    teamId = Column(String(3))
    lgID = Column(String(2))
    playerID = Column(String(9))
    G_all = Column(Integer)
    GS = Column(Integer)
    G_batting = Column(Integer)
    G_defense = Column(Integer)
    G_p = Column(Integer)
    G_c = Column(Integer)
    G_1b = Column(Integer)
    G_2b = Column(Integer)
    G_3b = Column(Integer)
    G_ss = Column(Integer)
    G_lf = Column(Integer)
    G_cf = Column(Integer)
    G_rf = Column(Integer)
    G_of = Column(Integer)
    G_dh = Column(Integer)
    G_ph = Column(Integer)
    G_pr = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.yearID = emptyStr(attributes[0])
        self.teamId = emptyStr(attributes[1])
        self.lgID = emptyStr(attributes[2])
        self.playerID = emptyStr(attributes[3])
        self.G_all = emptyInt(attributes[4])
        self.GS = emptyInt(attributes[5])
        self.G_batting = emptyInt(attributes[6])
        self.G_defense = emptyInt(attributes[7])
        self.G_p = emptyInt(attributes[8])
        self.G_c = emptyInt(attributes[9])
        self.G_1b = emptyInt(attributes[10])
        self.G_2b = emptyInt(attributes[11])
        self.G_3b = emptyInt(attributes[12])
        self.G_ss = emptyInt(attributes[13])
        self.G_lf = emptyInt(attributes[14])
        self.G_cf = emptyInt(attributes[15])
        self.G_rf = emptyInt(attributes[16])
        self.G_of = emptyInt(attributes[17])
        self.G_dh = emptyInt(attributes[18])
        self.G_ph = emptyInt(attributes[19])
        self.G_pr = emptyInt(attributes[20])

class Awards(BaseAwards):
    __tablename__ = "Awards"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    awardID = Column(String(255))
    yearID = Column(Integer)
    lgID = Column(String(2))
    tie = Column(String(2))
    notes = Column(String(100))

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.awardID = emptyStr(attributes[1])
        self.yearID = emptyInt(attributes[2])
        self.lgID = emptyStr(attributes[3])
        self.tie = emptyStr(attributes[4])
        self.notes = emptyStr(attributes[5])

class AwardsShare(BaseAwardsShare):
    __tablename__ = "AwardsShare"
    ID = Column(Integer, primary_key=True)
    awardID = Column(String(255))
    yearID = Column(Integer)
    lgID = Column(String(2))
    playerID = Column(String(9))
    pointsWon = Column(Numeric)
    pointsMax = Column(Integer)
    votesFirst = Column(Numeric)

    def __init__(self, line):
        attributes = line.split(",")
        self.awardID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.lgID = emptyStr(attributes[2])
        self.playerID = emptyStr(attributes[3])
        self.pointsWon = emptyFloat(attributes[4])
        self.pointsMax = emptyInt(attributes[5])
        self.votesFirst = emptyFloat(attributes[6])

class Batting(BaseBatting):
    __tablename__ = "Batting"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    stint = Column(Integer)
    teamID = Column(String(3))
    b_G = Column(Integer)
    b_AB = Column(Integer)
    b_R = Column(Integer)
    b_H = Column(Integer)
    b_2B = Column(Integer)
    b_3B = Column(Integer)
    b_HR = Column(Integer)
    b_RBI = Column(Integer)
    b_SB = Column(Integer)
    b_CS = Column(Integer)
    b_BB = Column(Integer)
    b_SO = Column(Integer)
    b_IBB = Column(Integer)
    b_HBP = Column(Integer)
    b_SH = Column(Integer)
    b_SF = Column(Integer)
    b_GIDP = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.stint = emptyInt(attributes[2])
        self.teamID = emptyStr(attributes[3])
        self.b_G = emptyInt(attributes[5])
        self.b_AB = emptyInt(attributes[6])
        self.b_R = emptyInt(attributes[7])
        self.b_H = emptyInt(attributes[8])
        self.b_2B = emptyInt(attributes[9])
        self.b_3B = emptyInt(attributes[10])
        self.b_HR = emptyInt(attributes[11])
        self.b_RBI = emptyInt(attributes[12])
        self.b_SB = emptyInt(attributes[13])
        self.b_CS = emptyInt(attributes[14])
        self.b_BB = emptyInt(attributes[15])
        self.b_SO = emptyInt(attributes[16])
        self.b_IBB = emptyInt(attributes[17])
        self.b_HBP = emptyInt(attributes[18])
        self.b_SH = emptyInt(attributes[19])
        self.b_SF = emptyInt(attributes[20])
        self.b_GIDP = emptyInt(attributes[21])

class BattingPost(BaseBattingPost):
    #should we rename attributes to bp_Attribute?
    __tablename__ = "BattingPost"
    ID = Column(Integer, primary_key=True)
    yearID = Column(Integer)
    round = Column(String(10))
    playerID = Column(String(9))
    teamID = Column(String(3))
    lgID = Column(String(2))
    bp_G = Column(Integer)
    bp_AB = Column(Integer)
    bp_R = Column(Integer)
    bp_H = Column(Integer)
    bp_2B = Column(Integer)
    bp_3B = Column(Integer)
    bp_HR = Column(Integer)
    bp_RBI = Column(Integer)
    bp_SB = Column(Integer)
    bp_CS = Column(Integer)
    bp_BB = Column(Integer)
    bp_SO = Column(Integer)
    bp_IBB = Column(Integer)
    bp_HBP = Column(Integer)
    bp_SH = Column(Integer)
    bp_SF = Column(Integer)
    bp_GIDP = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.yearID = emptyInt(attributes[0])
        self.round = emptyStr(attributes[1])
        self.playerID = emptyStr(attributes[2])
        self.teamID = emptyStr(attributes[3])
        self.lgID = emptyStr(attributes[4])
        self.bp_G = emptyInt(attributes[5])
        self.bp_AB = emptyInt(attributes[6])
        self.bp_R = emptyInt(attributes[7])
        self.bp_H = emptyInt(attributes[8])
        self.bp_2B = emptyInt(attributes[9])
        self.bp_3B = emptyInt(attributes[10])
        self.bp_HR = emptyInt(attributes[11])
        self.bp_RBI = emptyInt(attributes[12])
        self.bp_SB = emptyInt(attributes[13])
        self.bp_CS = emptyInt(attributes[14])
        self.bp_BB = emptyInt(attributes[15])
        self.bp_SO = emptyInt(attributes[16])
        self.bp_IBB = emptyInt(attributes[17])
        self.bp_HBP = emptyInt(attributes[18])
        self.bp_SH = emptyInt(attributes[19])
        self.bp_SF = emptyInt(attributes[20])
        self.bp_GIDP = emptyInt(attributes[21])

class Fielding(BaseFielding):
    __tablename__ = "Fielding"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    stint = Column(Integer)
    teamID = Column(String(3))
    lgID = Column(String(2))
    position = Column(String(2))
    f_G = Column(Integer)
    f_GS = Column(Integer)
    f_InnOuts = Column(Integer)
    f_PO = Column(Integer)
    f_A = Column(Integer)
    f_E = Column(Integer)
    f_DP = Column(Integer)
    f_PB = Column(Integer)
    f_WP = Column(Integer)
    f_SB = Column(Integer)
    f_CS = Column(Integer)
    f_ZR = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.stint = emptyInt(attributes[2])
        self.teamID = emptyStr(attributes[3])
        self.lgID = emptyStr(attributes[4])
        self.position = emptyStr(attributes[5])
        self.f_G = emptyInt(attributes[6])
        self.f_GS = emptyInt(attributes[7])
        self.f_InnOuts = emptyInt(attributes[8])
        self.f_PO = emptyInt(attributes[9])
        self.f_A = emptyInt(attributes[10])
        self.f_E = emptyInt(attributes[11])
        self.f_DP = emptyInt(attributes[12])
        self.f_PB = emptyInt(attributes[13])
        self.f_WP = emptyInt(attributes[14])
        self.f_SB = emptyInt(attributes[15])
        self.f_CS = emptyInt(attributes[16])
        self.f_ZR = emptyInt(attributes[17])

class FieldingPost(BaseFieldingPost):
    # should all attributes be renamed again
    __tablename__ = "FieldingPost"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    teamID = Column(String(3))
    lgID = Column(String(2))
    round = Column(String(10))
    position = Column(String(2))
    fp_G = Column(Integer)
    fp_GS = Column(Integer)
    fp_InnOuts = Column(Integer)
    fp_PO = Column(Integer)
    fp_A = Column(Integer)
    fp_E = Column(Integer)
    fp_DP = Column(Integer)
    fp_PB = Column(Integer)
    fp_WP = Column(Integer)
    fp_SB = Column(Integer)
    fp_CS = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.teamID = emptyStr(attributes[2])
        self.lgID = emptyStr(attributes[3])
        self.round = emptyStr(attributes[4])
        self.position = emptyStr(attributes[5])
        self.fp_G = emptyInt(attributes[6])
        self.fp_GS = emptyInt(attributes[7])
        self.fp_InnOuts = emptyInt(attributes[8])
        self.fp_PO = emptyInt(attributes[9])
        self.fp_A = emptyInt(attributes[10])
        self.fp_E = emptyInt(attributes[11])
        self.fp_DP = emptyInt(attributes[12])
        self.fp_PB = emptyInt(attributes[13])
        self.fp_WP = emptyInt(attributes[14])
        self.fp_SB = emptyInt(attributes[15])
        self.fp_CS = emptyInt(attributes[16])

class Franchises(BaseFranchises):
    __tablename__ = "Franchises"
    franchID = Column(String(3), primary_key=True)
    franchName = Column(String(50))
    active = Column(String(2))
    NAassoc = Column(String(3))

    def __init__(self, line):
        attributes = line.split(",")
        self.franchID = emptyStr(attributes[0])
        self.franchName = emptyStr(attributes[1])
        self.active = emptyStr(attributes[2])
        self.NAassoc = emptyStr(attributes[3])

class HomeGames(BaseHomeGames):
    __tablename__ = "HomeGames"
    ID = Column(Integer, primary_key=True)
    yearID = Column(Integer)
    lgID = Column(String(2))
    teamID = Column(String(3))
    parkID = Column(String(255))
    firstGame = Column(Date)
    lastGame = Column(Date)
    games = Column(Integer)
    openings = Column(Integer)
    attendance = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.yearID = emptyInt(attributes[0])
        self.lgID = emptyStr(attributes[1])
        self.teamID = emptyStr(attributes[2])
        self.parkID = emptyStr(attributes[3])
        firstGameStr = attributes[4].split("-")
        lastGameStr = attributes[5].split("-")
        self.games = emptyInt(attributes[6])
        self.openings = emptyInt(attributes[7])
        self.attendance = emptyInt(attributes[8])

        try:
            self.firstGame = emptyDate(firstGameStr[0], firstGameStr[1], firstGameStr[2])
        except Exception:
            self.firstGame = None

        try:
            self.lastGame = emptyDate(lastGameStr[0], lastGameStr[1], lastGameStr[2])
        except Exception:
            self.lastGame = None

class Manager(BaseManagers):
    __tablename__ = "Manager"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    teamID = Column(String(3))
    lgID = Column(String(2))
    inSeason = Column(Integer)
    manager_G = Column(Integer)
    manager_W = Column(Integer)
    manager_L = Column(Integer)
    teamRank = Column(Integer)
    plyrMgr = Column(String(1))

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.teamID = emptyStr(attributes[2])
        self.lgID = emptyStr(attributes[3])
        self.inSeason = emptyInt(attributes[4])
        self.manager_G = emptyInt(attributes[5])
        self.manager_W = emptyInt(attributes[6])
        self.manager_L = emptyInt(attributes[7])
        self.teamRank = emptyInt(attributes[8])
        self.plyrMgr = emptyStr(attributes[9])

class Park(BasePark):
    __tablename__ = "Park"
    ID = Column(Integer, primary_key=True)
    parkID = Column(String(255))
    park_name = Column(String(255))
    park_alias = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))

    def __init__(self, line):
        attributes = line.split(",")
        self.parkID = emptyStr(attributes[0])
        self.park_name = emptyStr(attributes[1])
        self.park_alias = emptyStr(attributes[2])
        self.city = emptyStr(attributes[3])
        self.state = emptyStr(attributes[4])
        self.country = emptyStr(attributes[5])

class People(BasePeople):
    __tablename__ = "People"
    playerID = Column(String(9), primary_key=True)
    birthYear = Column(Integer)
    birthMonth = Column(Integer)
    birthDay = Column(Integer)
    birthCountry = Column(String(255))
    birthState = Column(String(255))
    birthCity = Column(String(255))
    deathYear = Column(Integer)
    deathMonth = Column(Integer)
    deathDay = Column(Integer)
    deathCountry = Column(String(255))
    deathState = Column(String(255))
    deathCity = Column(String(255))
    nameFirst = Column(String(255))
    nameLast = Column(String(255))
    nameGiven = Column(String(255))
    weight = Column(Integer)
    height = Column(Integer)
    bats = Column(String(255))
    throws = Column(String(255))
    debutDate = Column(Date)
    finalGameDate = Column(Date)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.birthYear = emptyInt(attributes[1])
        self.birthMonth = emptyInt(attributes[2])
        self.birthDay = emptyInt(attributes[3])
        self.birthCountry = emptyStr(attributes[4])
        self.birthState = emptyStr(attributes[5])
        self.birthCity = emptyStr(attributes[6])
        self.deathYear = emptyInt(attributes[7])
        self.deathMonth = emptyInt(attributes[8])
        self.deathDay = emptyInt(attributes[9])
        self.deathCountry = emptyStr(attributes[10])
        self.deathState = emptyStr(attributes[11])
        self.deathCity = emptyStr(attributes[12])
        self.nameFirst = emptyStr(attributes[13])
        self.nameLast = emptyStr(attributes[14])
        self.nameGiven = emptyStr(attributes[15])
        self.weight = emptyInt(attributes[16])
        self.height = emptyInt(attributes[17])
        self.bats = emptyStr(attributes[18])
        self.throws = emptyStr(attributes[19])
        debutDateStr = attributes[20].split("-")
        finalGameDateStr = attributes[21].split("-")
        try:
            self.debutDate = emptyDate(debutDateStr[0], debutDateStr[1], debutDateStr[2])
        except Exception:
            self.debutDate = None
        
        try:
            self.finalGameDate = emptyDate(finalGameDateStr[0], finalGameDateStr[1], finalGameDateStr[2])
        except Exception:
            self.finalGameDate = None


class Pitching(BasePitching):
    __tablename__ = "Pitching"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    stint = Column(Integer)
    teamID = Column(String(3))
    lgID = Column(String(2))
    p_W = Column(Integer)
    p_L = Column(Integer)
    p_G = Column(Integer)
    p_GS = Column(Integer)
    p_CG = Column(Integer)
    p_SHO = Column(Integer)
    p_SV = Column(Integer)
    p_IPouts = Column(Integer)
    p_H = Column(Integer)
    p_ER = Column(Integer)
    p_HR = Column(Integer)
    p_BB = Column(Integer)
    p_SO = Column(Integer)
    p_BAOpp = Column(Double)
    p_ERA = Column(Double)
    p_BAOpp = Column(Numeric)
    p_ERA = Column(Numeric)
    p_IBB = Column(Integer)
    p_WP = Column(Integer)
    p_HBP = Column(Integer)
    p_BK = Column(Integer)
    p_BFP = Column(Integer)
    p_GF = Column(Integer)
    p_R = Column(Integer)
    p_SH = Column(Integer)
    p_SF = Column(Integer)
    p_GIDP = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.stint = emptyInt(attributes[2])
        self.teamID = emptyStr(attributes[3])
        self.lgID = emptyStr(attributes[4])
        self.p_W = emptyInt(attributes[5])
        self.p_L = emptyInt(attributes[6])
        self.p_G = emptyInt(attributes[7])
        self.p_GS = emptyInt(attributes[8])
        self.p_CG = emptyInt(attributes[9])
        self.p_SHO = emptyInt(attributes[10])
        self.p_SV = emptyInt(attributes[11])
        self.p_IPouts = emptyInt(attributes[12])
        self.p_H = emptyInt(attributes[13])
        self.p_ER = emptyInt(attributes[14])
        self.p_HR = emptyInt(attributes[15])
        self.p_BB = emptyInt(attributes[16])
        self.p_SO = emptyInt(attributes[17])
        self.p_BAOpp = emptyFloat(attributes[18])
        self.p_ERA = emptyFloat(attributes[19])
        self.p_IBB = emptyInt(attributes[20])
        self.p_WP = emptyInt(attributes[21])
        self.p_HBP = emptyInt(attributes[22])
        self.p_BK = emptyInt(attributes[23])
        self.p_BFP = emptyInt(attributes[24])
        self.p_GF = emptyInt(attributes[25])
        self.p_R = emptyInt(attributes[26])
        self.p_SH = emptyInt(attributes[27])
        self.p_SF = emptyInt(attributes[28])
        self.p_GIDP = emptyInt(attributes[29])

class PitchingPost(BasePitchingPost):
    __tablename__ = "PitchingPost"
    ID = Column(Integer, primary_key=True)
    playerID = Column(String(9))
    yearID = Column(Integer)
    round = Column(String(10))
    teamID = Column(String(3))
    lgID = Column(String(2))
    pp_W = Column(Integer)
    pp_L = Column(Integer)
    pp_G = Column(Integer)
    pp_GS = Column(Integer)
    pp_CG = Column(Integer)
    pp_SHO = Column(Integer)
    pp_SV = Column(Integer)
    pp_IPouts = Column(Integer)
    pp_H = Column(Integer)
    pp_ER = Column(Integer)
    pp_HR = Column(Integer)
    pp_BB = Column(Integer)
    pp_SO = Column(Integer)
    pp_BAOpp = Column(Numeric)
    pp_ERA = Column(Numeric)
    pp_IBB = Column(Integer)
    pp_WP = Column(Integer)
    pp_HBP = Column(Integer)
    pp_BK = Column(Integer)
    pp_BFP = Column(Integer)
    pp_GF = Column(Integer)
    pp_R = Column(Integer)
    pp_SH = Column(Integer)
    pp_SF = Column(Integer)
    pp_GIDP = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.playerID = emptyStr(attributes[0])
        self.yearID = emptyInt(attributes[1])
        self.round = emptyStr(attributes[2])
        self.teamID = emptyStr(attributes[3])
        self.lgID = emptyStr(attributes[4])
        self.pp_W = emptyInt(attributes[5])
        self.pp_L = emptyInt(attributes[6])
        self.pp_G = emptyInt(attributes[7])
        self.pp_GS = emptyInt(attributes[8])
        self.pp_CG = emptyInt(attributes[9])
        self.pp_SHO = emptyInt(attributes[10])
        self.pp_SV = emptyInt(attributes[11])
        self.pp_IPouts = emptyInt(attributes[12])
        self.pp_H = emptyInt(attributes[13])
        self.pp_ER = emptyInt(attributes[14])
        self.pp_HR = emptyInt(attributes[15])
        self.pp_BB = emptyInt(attributes[16])
        self.pp_SO = emptyInt(attributes[17])
        self.pp_BAOpp = emptyFloat(attributes[18])
        self.pp_ERA = emptyFloat(attributes[19])
        self.pp_IBB = emptyInt(attributes[20])
        self.pp_WP = emptyInt(attributes[21])
        self.pp_HBP = emptyInt(attributes[22])
        self.pp_BK = emptyInt(attributes[23])
        self.pp_BFP = emptyInt(attributes[24])
        self.pp_GF = emptyInt(attributes[25])
        self.pp_R = emptyInt(attributes[26])
        self.pp_SH = emptyInt(attributes[27])
        self.pp_SF = emptyInt(attributes[28])
        self.pp_GIDP = emptyInt(attributes[29])

class Salary(BaseSalary):
    __tablename__ = "Salary"
    ID = Column(Integer, primary_key=True)
    yearID = Column(Integer)
    teamID = Column(String(3))
    lgID = Column(String(2))
    playerID = Column(String(9))
    salary = Column(Integer)
    
    def __init__(self, line):
        attributes = line.split(",")
        self.yearID = emptyInt(attributes[0])
        self.teamID = emptyStr(attributes[1])
        self.lgID = emptyStr(attributes[2])
        self.playerID = emptyStr(attributes[3])
        self.salary = emptyInt(attributes[4])

class School(BaseSchool):
    __tablename__ = "School"
    schoolID = Column(String(64), primary_key=True)
    name_full = Column(String(55))
    city = Column(String(55))
    state = Column(String(2))
    country = Column(String(55))
    
    def __init__(self, line):
        attributes = line.split(",")
        self.schoolID = emptyStr(attributes[0])
        self.name_full = emptyStr(attributes[1])
        self.city = emptyStr(attributes[2])
        self.state = emptyStr(attributes[3])
        self.country = emptyStr(attributes[4])

class SeriesPost(BaseSeriesPost):
    __tablename__ = "SeriesPost"
    ID = Column(Integer, primary_key=True)
    teamIDwinner = Column(String(3))
    teamIDloser = Column(String(3))
    yearID = Column(Integer)
    round = Column(String(5))
    wins = Column(Integer)
    loses = Column(Integer)
    ties = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.teamIDwinner = emptyStr(attributes[2])
        self.teamIDloser = emptyStr(attributes[4])
        self.yearID = emptyInt(attributes[0])
        self.round = emptyStr(attributes[1])
        self.wins = emptyInt(attributes[6])
        self.loses = emptyInt(attributes[7])
        self.ties = emptyInt(attributes[8])

class Strikes(BaseStrikes):
    __tablename__ = "Strikes"
    ID = Column(Integer, primary_key=True)
    name = Column(String(64))
    start_date = Column(Date)
    end_date = Column(Date)
    games_cancelled = Column(Integer)
    schedule_effects = Column(String(255))
    issues_of_contention = Column(String(255))
    commissioner = Column(String(255))

    def __init__(self, line):
        attributes = line.split(",")
        self.name = emptyStr(attributes[0])
        startDateStr = attributes[1].split("-")
        endDateStr = attributes[2].split("-")
        self.games_cancelled = emptyInt(attributes[3])
        self.schedule_effects = emptyStr(attributes[4])
        self.issues_of_contention = emptyStr(attributes[5])
        self.commissioner = emptyStr(attributes[6])

        try:
            self.start_date = emptyDate(startDateStr[0], startDateStr[1], startDateStr[2])
        except Exception:
            self.start_date = None

        try:
            self.end_date = emptyDate(endDateStr[0], endDateStr[1], endDateStr[2])
        except Exception:
            self.end_date = None

class Team(BaseTeam):
    __tablename__ = "Team"
    ID = Column(Integer, primary_key=True)
    teamID = Column(String(3))
    yearID = Column(Integer)
    lgID = Column(String(2))
    divID = Column(String(1))
    franchID = Column(String())
    name = Column(String(50))
    teamRank = Column(Integer)
    team_G = Column(Integer)
    team_G_home = Column(Integer)
    team_W = Column(Integer)
    team_L = Column(Integer)
    DivWin = Column(String(1))
    WCWin = Column(String(1))
    LgWin = Column(String())
    WSWin  = Column(String(1))
    team_R = Column(Integer)
    team_AB = Column(Integer)
    team_H = Column(Integer)
    team_2B = Column(Integer)
    team_3B = Column(Integer)
    team_HR = Column(Integer)
    team_BB = Column(Integer)
    team_SO = Column(Integer)
    team_SB = Column(Integer)
    team_CS = Column(Integer)
    team_HBP = Column(Integer)
    team_SF = Column(Integer)
    team_RA = Column(Integer)
    team_ER = Column(Integer)
    team_ERA = Column(Numeric)
    team_CG = Column(Integer)
    team_SHO = Column(Integer)
    team_SV = Column(Integer)
    team_IPouts = Column(Integer)
    team_HA = Column(Integer)
    team_HRA = Column(Integer)
    team_BBA = Column(Integer)
    team_SOA = Column(Integer)
    team_E = Column(Integer)
    team_DP = Column(Integer)
    team_FP = Column(Numeric)
    park = Column(String(255))
    attendance = Column(Numeric)
    team_BFP = Column(Integer)

    def __init__(self, line):
        attributes = line.split(",")
        self.yearID = emptyInt(attributes[0])
        self.lgID = emptyStr(attributes[1])
        self.teamID = emptyStr(attributes[2])
        self.franchID = emptyStr(attributes[3])
        self.divID = emptyStr(attributes[4])
        self.teamRank = emptyInt(attributes[5])
        self.team_G = emptyInt(attributes[6])
        self.team_G_home = emptyInt(attributes[7])
        self.team_W = emptyInt(attributes[8])
        self.team_L = emptyInt(attributes[9])
        self.DivWin = emptyStr(attributes[10])
        self.WCWin = emptyStr(attributes[11])
        self.LgWin = emptyStr(attributes[12])
        self.WSWin  = emptyStr(attributes[13])
        self.team_R = emptyInt(attributes[14])
        self.team_AB = emptyInt(attributes[15])
        self.team_H = emptyInt(attributes[16])
        self.team_2B = emptyInt(attributes[17])
        self.team_3B = emptyInt(attributes[18])
        self.team_HR = emptyInt(attributes[19])
        self.team_BB = emptyInt(attributes[20])
        self.team_SO = emptyInt(attributes[21])
        self.team_SB = emptyInt(attributes[22])
        self.team_CS = emptyInt(attributes[23])
        self.team_HBP = emptyInt(attributes[24])
        self.team_SF = emptyInt(attributes[25])
        self.team_RA = emptyInt(attributes[26])
        self.team_ER = emptyInt(attributes[27])
        self.team_ERA = emptyFloat(attributes[28])
        self.team_CG = emptyInt(attributes[29])
        self.team_SHO = emptyInt(attributes[30])
        self.team_SV = emptyInt(attributes[31])
        self.team_IPouts = emptyInt(attributes[32])
        self.team_HA = emptyInt(attributes[33])
        self.team_HRA = emptyInt(attributes[34])
        self.team_BBA = emptyInt(attributes[35])
        self.team_SOA = emptyInt(attributes[36])
        self.team_E = emptyInt(attributes[37])
        self.team_DB = emptyInt(attributes[38])
        self.team_FP = emptyFloat(attributes[39])
        self.name = emptyStr(attributes[40])
        self. park = emptyStr(attributes[41])
        self.attendance = emptyFloat(attributes[42])
        self.team_BFP = emptyInt(attributes[43])

# begin to LOAD data
def initAllStar():
    # configure database
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
    session.execute("DELETE FROM allstarfull")
    session.commit()    

    # begin to read through the file
    file = open("./baseballdatabank2022/core/AllstarFull.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # allStar = session.query(AllStar).filter_by().first()
        session.add(AllStar(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initAppearances():
    # configure database
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
    session.execute("DELETE FROM appearances")
    session.commit() 

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Appearances.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # appearance = session.query(Appearances).filter_by().first()
        session.add(Appearances(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initAwards():
    # configure database
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
    session.execute("DELETE FROM awards")
    session.commit() 

    # begin to read through the file
    file = open("./baseballdatabank2022/contrib/AwardsPlayers.csv", "r")
    fileManagers = open("./baseballdatabank2022/contrib/AwardsManagers.csv", "r")
    next(file)
    next(fileManagers)
    for player in file:
        # syntax for query
        # appearance = session.query(Appearances).filter_by().first()
        session.add(Awards(player))
    
    for manager in fileManagers:
        session.add(Awards(manager))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()
    fileManagers.close()

def initAwardsShare():
    # configure database
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
    session.execute("DELETE FROM awardsshare")
    session.commit() 

    # begin to read through the file
    file = open("./baseballdatabank2022/contrib/AwardsSharePlayers.csv", "r")
    fileManagers = open("./baseballdatabank2022/contrib/AwardsShareManagers.csv", "r")
    next(file)
    next(fileManagers)
    for player in file:
        # syntax for query
        # appearance = session.query(Appearances).filter_by().first()
        session.add(AwardsShare(player))
    
    for manager in fileManagers:
        session.add(AwardsShare(manager))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()
    fileManagers.close()

def initBatting():
    # configure database
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
    session.execute("DELETE FROM batting")
    session.commit() 

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Batting.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # batter = session.query(Batting).filter_by().first()
        session.add(Batting(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initBattingPost():
    # configure database
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
    session.execute("DELETE FROM battingpost")
    session.commit() 

    # begin to read through the file
    file = open("./baseballdatabank2022/core/BattingPost.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # batterPost = session.query(BattingPost).filter_by().first()
        session.add(BattingPost(player))
    
    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initFielding():
    # configure database
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
    session.execute("DELETE FROM fielding")
    session.commit() 

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Fielding.csv", "r")
    fileSplit = open("./baseballdatabank2022/core/FieldingOFSplit.csv", "r")
    next(file)
    next(fileSplit)
    
    # add infielders and outfielders before 1954
    for player in file:
        attributes = player.split(",")
        if(attributes[5] != "OF"):
            session.add(Fielding(player))
        elif(attributes[5] == "OF" and int(attributes[1]) < 1954):
            session.add(Fielding(player))
    
    # add outfielders after 1954
    for outfielder in fileSplit:
        session.add(Fielding(outfielder))
            

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()
    fileSplit.close()

def initFieldingPost():
    # configure database
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
    session.execute("DELETE FROM fieldingpost")
    session.commit()    

    # begin to read through the file
    file = open("./baseballdatabank2022/core/FieldingPost.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # fielderPost = session.query(BattingPost).filter_by().first()
        session.add(FieldingPost(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initFranchises():
    # configure database
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
    session.execute("DELETE FROM franchises")
    session.commit()    

    # begin to read through the file
    file = open("./baseballdatabank2022/core/TeamsFranchises.csv", "r")
    next(file)
    for franchise in file:
        # syntax for query
        # franchise = session.query(Franchises).filter_by().first()
        session.add(Franchises(franchise))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initHomeGames():
    # configure database
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
    session.execute("DELETE FROM homegames")
    session.commit()    

    # begin to read through the file
    file = open("./baseballdatabank2022/core/HomeGames.csv", "r")
    next(file)
    for game in file:
        # syntax for query
        # game = session.query(HomeGames).filter_by().first()
        session.add(HomeGames(game))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initManager():
    # configure database
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
    session.execute("DELETE FROM manager")
    session.commit()    

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Managers.csv", "r")
    
    next(file)
    for manager in file:
        # syntax for query
        # fielderPost = session.query(Managers).filter_by().first()
        session.add(Manager(manager))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initPark():
    # configure database
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
    session.execute("DELETE FROM park")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Parks.csv", "r")
    next(file)
    for park in file:
        # syntax for query
        # fielderPost = session.query(Parks).filter_by().first()
        session.add(Park(park))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initPeople():
    # configure database
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
    session.execute("DELETE FROM people")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/People.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # fielderPost = session.query(People).filter_by().first()
        session.add(People(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()


def initPitching():
    # configure database
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
    session.execute("DELETE FROM pitching")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Pitching.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # fielderPost = session.query(Pitching).filter_by().first()
        session.add(Pitching(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initPitchingPost():
    # configure database
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
    session.execute("DELETE FROM pitchingpost")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/PitchingPost.csv", "r")
    next(file)
    for player in file:
        # syntax for query
        # fielderPost = session.query(PitchingPost).filter_by().first()
        session.add(PitchingPost(player))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initSalary():
    # configure database
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
    session.execute("DELETE FROM salary")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/contrib/Salaries.csv", "r")
    next(file)
    for salary in file:
        # syntax for query
        session.add(Salary(salary))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()


def initSchool():
    # configure database
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
    session.execute("DELETE FROM school")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/contrib/Schools.csv", "r")
    next(file)
    for school in file:
        # syntax for query
        session.add(School(school))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initSeriesPost():
    # configure database
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
    session.execute("DELETE FROM seriespost")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/SeriesPost.csv", "r")
    next(file)
    for series in file:
        # syntax for query
        # fielderPost = session.query(SeriesPost).filter_by().first()
        session.add(SeriesPost(series))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initStrikes():
    # configure database
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
    session.execute("DELETE FROM strikes")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Strikes.csv", "r")
    next(file)
    for strike in file:
        # syntax for query
        # fielderPost = session.query(SeriesPost).filter_by().first()
        session.add(Strikes(strike))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

def initTeam():
    # configure database
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
    session.execute("DELETE FROM team")
    session.commit()  

    # begin to read through the file
    file = open("./baseballdatabank2022/core/Teams.csv", "r")
    next(file)
    for team in file:
        # syntax for query
        # fielderPost = session.query(Team).filter_by().first()
        session.add(Team(team))

    # commit changes and close the connection
    session.commit()
    session.close()

    file.close()

# call all init functions
initPeople()
initAllStar()
initAppearances()
initAwards()
initAwardsShare()
initBatting()
initBattingPost()
initFielding()
initFieldingPost()
initFranchises()
initHomeGames()
initManager()
initPark()
initPitching()
initPitchingPost()
initSalary()
initSchool()
initSeriesPost()
initStrikes()
initTeam()
initHallOfFame()
