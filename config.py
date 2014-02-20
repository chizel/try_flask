import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://fordb:qwerty@localhost/pdb'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#WHOOSH_BASE = os.path.join(basedir, 'search.db')
WHOOSH_BASE = 'postgresql://fordb:qwerty@localhost/pdb'

RF_ENABLED = True
SECRET_KEY = 'very-strange-key'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
    { 'name': 'StackExchange', 'url': 'https://openid.stackexchange.com' }]

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['chizel@inbox.ru']

# pagination
POSTS_PER_PAGE = 3
