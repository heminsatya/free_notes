# Dependencies
from aurora import Controller, View

# The controller class
class AccessDenied(Controller):

	# HTTP GET Method
    def get(self):
        return View('403', code=403)
