#-*- coding:utf-8 -*-
import os

#set debug
DEBUG = True

#set session salt
SECKET_KEY = os.urandom(24)

#set mysql url
HOSTNAME = '127.0.0.1'
PORT = '3306'
USER = 'root'
PASSWORD = ''
DATABASE = 'flask_db'
DB_RUL = 'mysql://{}:{}@{}/{}?charset=utf8'.format(USER,PASSWORD,HOSTNAME,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_RUL
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

