# Dependencies
from aurora import Controller, View

# The controller class
class BadRequest(Controller):

	# HTTP GET Method
    def get(self):
        return View('400', code=400)
