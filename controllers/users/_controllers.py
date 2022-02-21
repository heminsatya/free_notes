# Dependencies
from aurora.helpers import controller

# Controllers routes
controllers = [
    controller(name='Login', url='', methods=['GET', 'POST']),
    controller(name='Login', url='login', methods=['GET', 'POST']),
    controller(name='Register', url='register', methods=['GET', 'POST']),
    controller(name='Logout', url='logout', methods=['GET']),
]#do-not-change-me
