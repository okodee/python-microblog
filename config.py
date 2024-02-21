import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'database.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-will-never-guess'
MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
MAIL_PORT = 2525
MAIL_USERNAME = '4f12ecd93bc72f'
MAIL_PASSWORD = 'bfeaacdd152c31'
ADMIN = ['33e70c3596-15831e+1@inbox.mailtrap.io']
MAIL_USE_TLS = True
MAIL_USE_SSL = False