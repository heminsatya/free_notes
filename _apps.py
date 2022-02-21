# Dependencies
from aurora.helpers import app

# Controllers routes
apps = [
    app(name='errors', url='errors'),
    app(name='aurora', url='aurora'),
    app(name='notes', url='notes'),
    app(name='users', url='users'),
]#do-not-change-me