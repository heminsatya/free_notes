# Dependencies
from aurora import Controller, View
from aurora import __version__

# The controller class
class Index(Controller):

	# HTTP GET Method
    def get(self):
        return View('index', version = __version__)
