# Dependencies
from aurora import Controller, View

# The controller class
class MethodForbidden(Controller):

	# HTTP GET Method
    def get(self):
        return View('405', code=405)
