import os
from pathlib import Path
import random
import string

basedir = Path(__file__).parent.absolute()

def random_string(k):
    source = string.ascii_letters + string.digits
    return ''.join(random.choices(source, k=k))

class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or random_string(24)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    EMAIL_FROM_ADDR = os.environ.get('EMAIL_FROM_ADDR')
    EMAIL_SMTP_SERV = os.environ.get('EMAIL_SMTP_SERV')
    DOMAIN = os.environ.get('PUBLIC_DOMAIN')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{basedir}/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = 'pages'

    MAPSERVER_URL = os.environ.get('MAPSERVER_URL') or \
        'https://www.geos.ed.ac.uk/maps/mhagdorn/cresh?'
