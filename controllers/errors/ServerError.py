# Dependencies
from aurora import Controller, View

# The controller class
class ServerError(Controller):

	# HTTP GET Method
    def get(self):
        return View('500', code=500)
