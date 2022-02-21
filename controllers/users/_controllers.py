# Dependencies
from aurora.helpers import router

# Controllers routes
controllers = [
    router(controller='Login', methods=['GET', 'POST']),
    router(controller='Login', url='login', methods=['GET', 'POST']),
    router(controller='Register', url='register', methods=['GET', 'POST']),
    router(controller='Logout', url='logout'),
]#do-not-change-me
