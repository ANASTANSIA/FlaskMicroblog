import os
basedir = os.path.abspath(os.path.dirname(__file__))

# class that stores configuration variables
class Config(object):
    # configuration settings defined as class variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # secret key value is sometimes used as a cryptographic key  ,usefull yo generate tokenns or signatures
    # used by web forms to  protect web forms against cross site request forgery
    
    # Sqlite database using sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False