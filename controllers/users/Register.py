# Dependencies
import importlib
from aurora import Controller, View, Forms
from models import Users
from aurora.security import request, login_abort, hash_password, set_session

# The controller class
class Register(Controller):

    # Constructor
    def __init__(self):
        super().__init__()
        
        # Models
        self.users  = Users()
        self.consts = importlib.import_module(f'helpers.consts.{self.active_lang}')


    # POST Method
    @login_abort('notes')
    def post(self):
        # Form data
        data = request.form
        form = Forms(data)

        # Valid form data
        if form.validate():
            # Collect form inputs
            username = data.get('username')
            email    = data.get('email')
            password = data.get('password')
            confirm  = data.get('confirm')

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
            if self.users.read(where={'username':username}).count():
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Username already registered!',
                }, 400

            # Check email
            if self.users.read(where={'email':email}).count():
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Email already registered!',
                }, 400

            # Everything is fine
            # Insert user into database
            data = {
                'username': username,
                'email':    email,
                'password': hash_password(password),
            }
            self.users.create(data=data)

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
        return View('register', form=form, consts=self.consts, LANGUAGE=self.LANGUAGE)
