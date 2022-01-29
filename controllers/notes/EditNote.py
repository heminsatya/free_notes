# Dependencies
from aurora import Controller, View, Forms
from models import Users, Notes
from aurora.security import login_required, get_session
from flask import request

# The controller class
class EditNote(Controller):

    # GET Method
    @login_required(app='users')
    def get(self, id=None):
        # The required models
        user = Users().read(where={'username':get_session('user')}).first()
        note = Notes().read(where={'id':id, 'user_id':user['id']}).first()

        form = Forms()

        return View('update', user=user, note=note, form=form)


    # PUT Method
    @login_required(app='users')
    def put(self):
        # The required models
        user = Users().read(where={'username':get_session('user')}).first()
        notes = Notes()

        # Form data
        data = request.form
        form = Forms(data)

        # Valid form data
        if form.validate():
            # Collect form inputs
            title = data.get('title')
            content = data.get('content')
            id = data.get('id')

            # Required fields
            if not title or not content:
                return {
                    'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
                }, 400

            # Check if the note is users' note
            if notes.read(where={'id':id, 'user_id':user['id']}).count() != 1:
                return {
                    'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Forbidden data requested!',
                }, 400

            # Everything is fine
            # Update note to the database
            data = {
                'title': title,
                'content': content
            }
            notes.update(data=data, where={'id':id})

            # Return the result
            return {
                'success': '<i class="fas fa-check-circle mr-1"></i> The note updated successfully!',
            }, 200

        # Invalid form data
        else:
            # Return the result
            return {
                'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
            }, 400

