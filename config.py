import os
basedir = os.path.abspath(os.path.dirname(__file__))
import csi3335sp2022 as cfg
import pymysql

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-secret'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+cfg.mysql['user']+":"+cfg.mysql['password']+"@"+cfg.mysql['host']+":3306/" +cfg.mysql['db']

    SQLALCHEMY_TRACK_MODIFICATIONS = False
