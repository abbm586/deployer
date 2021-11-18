from os import environ, path


basedir = path.abspath(path.dirname(__file__))

class Config():

    DEBUG = True
    # Set up the App SECRET_KEY
    SECRET_KEY = 'S#per-Cr3D1t_S3crEt_007'

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

