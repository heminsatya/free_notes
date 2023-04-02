# Dependencies
import importlib
from aurora import Controller, View
from aurora.security import login_abort


# The controller class
class Index(Controller):

    # Constructor
    def __init__(self):
        super().__init__()
        
        self.consts = importlib.import_module(f'helpers.consts.{self.active_lang}')


    # GET Method
    @login_abort(app='notes', controller='Notes')
    def get(self):
        print(self.consts)
        return View('index', LANGUAGE=self.LANGUAGE, consts=self.consts)
