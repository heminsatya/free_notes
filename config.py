# Dependencies
import os
import platform
from aurora.helpers import random_string


# Root app path
ROOT_PATH = os.path.dirname(__file__)


# Path separator
if platform.system() == 'Windows':
    SEP = '\\'

# Unix
else:
    SEP = '/'


# The error app to handle http errors (Auto Global)
ERROR_APP = 'errors'


# The default app to serve the '/' url (Auto Global)
DEFAULT_APP = 'notes'


# Static Files (Auto Global)
STATICS = 'statics'


# Development mode
DEVELOPMENT = True       # True | False


# For development
if DEVELOPMENT:
    HOST  = '127.1.1.1'
    PORT  = '5000'
    DEBUG = True

# For production deployment
else:
    HOST  = '0.0.0.0'
    PORT  = '5000'
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
        'password': 'db_password',
        'database': 'app_db',
    }

# Postgres Database
elif DB_SYSTEM == 'Postgres':
    DB_CONFIG = {
        'host':     'localhost',
        'user':     'postgres',
        'password': 'db_password',
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
"""
For Unix use 'Europe/London', 'Asia/Tokyo', etc! (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
For windows use 'Central Standard Time', 'GMT Standard Time', 'Tokyo Standard Time' etc (https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones).
@Warning! For windows it will alter Windows system time. To avoid this set it to '' (empty string).
"""
TIMEZONE = ''


# Default language
DEFAULT_LANG = 'en'


# Multi language
MULTI_LANG = False      # True | False


# Available laguages
LANGUAGES = (
    'en',   # English
)


# Maximum upload size for server (bytes)
UPLOAD_SIZE = 16 * 1024 * 1024      # 16 MB


# Allowed upload extensions
UPLOAD_TYPES = ['.webp', '.jpg', '.jpeg', '.apng', '.png', '.avif', '.gif', '.svg', '.mp3', '.ogg', '.weba', '.aac', '.wav', '.mp4', '.webm', '.txt', '.pdf']


# Upload Path
UPLOAD_PATH = ROOT_PATH + SEP + STATICS +  SEP + 'upload'


# Global variables
GLOBALS = {
    'key': 'Value',
}


# Project version
VERSION = "1.3.0"
