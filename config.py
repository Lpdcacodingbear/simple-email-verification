from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY') or 'you-will-never-guess'
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PROT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')