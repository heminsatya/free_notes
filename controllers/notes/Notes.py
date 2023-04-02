# Dependencies
import importlib
from aurora import Controller, View
from models import Users, Notes as NotesModel
from aurora.security import request, get_session, login_required


# The controller class
class Notes(Controller):

    # Constructor
    def __init__(self):
        super().__init__()
        
        # Models
        self.users = Users()
        self.notes = NotesModel()
        
        # Models objects
        self.consts = importlib.import_module(f'helpers.consts.{self.active_lang}')


    # GET Method
    @login_required(app='users')
    def get(self):
        user  = self.users.read(where={'username':get_session('user')}).first()
        notes = NotesModel().read(where={'user_id':user['id']}, order_by={'id':'DESC'}).all()

        return View('notes', user=user, notes=notes, LANGUAGE=self.LANGUAGE, consts=self.consts)


    # DELETE Method
    @login_required(app='users')
    def delete(self):
        user = self.users.read(where={'username':get_session('user')}).first()

        # Form data
        data = request.json
        id   = data['id']

        # Check if the note is users' note
        if self.notes.read(where={'id':id, 'user_id':user['id']}).count() != 1:
            return {
                'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Forbidden data requested!',
            }, 400

        # Everything is fine
        # Delete note from the database
        self.notes.delete(where={'id':id})

        # Return the result
        return {
            'success': '<i class="fas fa-check-circle mr-1"></i> The note deleted successfully!',
        }, 200
