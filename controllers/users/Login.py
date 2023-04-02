# Dependencies
import importlib
from aurora import Controller, View, Forms
from models import Users
from aurora.security import request, login_abort, validate_password, set_session, set_cookie


# The controller class
class Login(Controller):

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
            password = data.get('password')
            remember = data.get('remember')
            next     = data['next']
            url      = next if next else '/'

            # Required fields
            if not username or not password:
                return {
                    'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
                }, 400

            # Check the database
            try:
                user_count  = self.users.read(where={'username':username}).count()
                db_password = self.users.read(where={'username':username}).first()['password']

            except:
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Invalid username and/or password!',
                }, 400

            # Authenticate user
            # Valid user
            if user_count == 1 and validate_password(db_password, password):

                # Set the user session
                set_session('user', username)

                res = {
                    'success': '<i class="fas fa-check-circle mr-1"></i> Login was successful!',
                    'url': f'{url}'
                }

                # Check remember me
                if remember == "on":
                    data = {'type': 'json', 'response': res}
                    res = set_cookie('user', username, data)

                # Return the result
                return res, 200

            # Invalid user
            else:
                return {
                    'error': '<i class="fas fa-exclamation-circle mr-1"></i> Invalid username and/or password!',
                }, 400

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

        # Check next url
        if 'next' in request.url:
            next = request.args.get('next')
        else:
            next = ''

        return View('login', form=form, next=next, consts=self.consts, LANGUAGE=self.LANGUAGE)
