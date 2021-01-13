from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY') or 'you-will-never-guess'
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False