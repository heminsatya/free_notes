# Dependencies
import os
from aurora.helpers import random_string


# Root app path
ROOT_PATH = os.path.dirname(__file__)


# The error app to handle http errors (Auto Global)
ERROR_APP = 'errors'


# The default app to serve the '/' url (Auto Global)
DEFAULT_APP = 'notes'


# Static Files (Auto Global)
STATICS = 'statics'


# Development mode
DEVELOPMENT = True


# For development
if DEVELOPMENT:
    HOST  = '127.1.1.1'
    PORT  = '5000'
    DEBUG = True

# For production deployment
else:
    HOST  = 'yourwebsite.com'
    PORT  = '8080'
    DEBUG = False


# Database System
DB_SYSTEM = 'SQLite'    # 'SQLite', 'MySQL', 'Postgres'


# Check the Database System
# SQLite Database
if DB_SYSTEM == 'SQLite':
    DB_CONFIG = {
        'database': 'app.db',
    }

# MySQL Database
elif DB_SYSTEM == 'MySQL':
    DB_CONFIG = {
        'host':     'localhost',
        'user':     'root',
        'password': 'mspass123456',     # db_password
        'database': 'app_db',
    }

# Postgres Database
elif DB_SYSTEM == 'Postgres':
    DB_CONFIG = {
        'host':     'localhost',
        'user':     'postgres',
        'password': 'pspass123456',     # db_password
        'database': 'app_db',
        'port':     '5432',
    }


# Database API Engine
DB_ENGINE = 'AuroraSQL'    # 'AuroraSQL'


# Database Safe Typing
SAFE_TYPE = True


# FORM API Engine
FORM_ENGINE = 'WTForms'    # 'WTForms'


# App Secret Key
SECRET_KEY = random_string(24)


# Timezone
TIMEZONE = 'Central Standard Time'  # 'Central Standard Time', 'Europe/London', 'Asia/Tokyo', ...


# Default language
DEFAULT_LANG = 'en'


# Multi language
MULTI_LANG = False      # True | False


# For multi language
if MULTI_LANG:
    # Available langs
    LANGS = [
        'en',   # English
    ]


# Global variables
GLOBALS = {
    'key': 'Value',
}


# Project version
VERSION = "1.2.0"
