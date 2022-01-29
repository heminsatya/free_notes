# Dependencies
from aurora import Controller, View

# The controller class
class NotFound(Controller):

	# HTTP GET Method
    def get(self):
        return View('404', code=404)
