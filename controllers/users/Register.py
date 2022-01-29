# Dependencies
from aurora import Controller, View, Forms
from models import Users
from flask import request
from aurora.security import login_abort, hash_password, set_session

# The controller class
class Register(Controller):

    # POST Method
    @login_abort('notes')
    def post(self):
        # The Users model
        users = Users()

        # Form data
        data = request.form
        form = Forms(data)

        # Valid form data
        if form.validate():
            # Collect form inputs
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            confirm = data.get('confirm')

            # Required fields
            if not username or not email or not password or not confirm:
                return {
                    'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
                }, 400

            # Passwords length
            if len(password) < 6:
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Password must be at least 6 characters!',
                }, 400

            # Check passwords
            if password != confirm:
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Passwords not match!',
                }, 400

            # Check username
            if users.read(where={'username':username}).count():
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Username already registered!',
                }, 400

            # Check email
            if users.read(where={'email':email}).count():
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Email already registered!',
                }, 400

            # Everything is fine
            # Insert user into database
            data = {
                'username': username,
                'email': email,
                'password': hash_password(password),
            }
            users.create(data=data)

            # Set the user session
            set_session('user', username)

            # Return the result
            return {
                'success': '<i class="fas fa-check-circle mr-1"></i> Registration was successful!',
            }, 200

        # Invalid form data
        else:
            # Return the result
            return {
                'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
            }, 400


    # GET Method
    @login_abort('notes')
    def get(self):
        form = Forms()
        return View('register', form=form)

