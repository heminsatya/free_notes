# Dependencies
from aurora import Controller, View
from aurora.security import login_abort

# The controller class
class Index(Controller):

    # GET Method
    @login_abort(app='notes', controller='Notes')
    def get(self):
        return View('index')

