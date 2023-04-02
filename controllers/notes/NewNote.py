# Dependencies
import importlib
from aurora import Controller, View, Forms
from models import Users, Notes
from aurora.security import request, login_required, get_session


# The controller class
class NewNote(Controller):

    # Constructor
    def __init__(self):
        super().__init__()
        
        # Models
        self.users = Users()
        self.notes = Notes()
        
        # Models objects
        self.consts = importlib.import_module(f'helpers.consts.{self.active_lang}')


    # POST Method
    @login_required(app='users')
    def post(self):
        user = self.users.read(where={'username':get_session('user')}).first()

        # Form data
        data = request.form
        form = Forms(data)

        # Valid form data
        if form.validate():
            # Collect form inputs
            title = data.get('title')
            content = data.get('content')

            # Required fields
            if not title or not content:
                return {
                    'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
                }, 400

            # Everything is fine
            # Insert new note into the database
            data = {
                'user_id': user['id'],
                'title':   title,
                'content': content,
                # 'date':    datetime.now().strftime("%m-%d-%Y")
            }
            self.notes.create(data=data)

            # Return the result
            return {
                'success': '<i class="fas fa-check-circle mr-1"></i> The new note created successfully!',
            }, 200

        # Invalid form data
        else:
            # Return the result
            return {
                'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
            }, 400


    # GET Method
    @login_required(app='users')
    def get(self):
        form = Forms()
        user = self.users.read(where={'username':get_session('user')}).first()
        
        return View('create', form=form, user=user, LANGUAGE=self.LANGUAGE, consts=self.consts)
