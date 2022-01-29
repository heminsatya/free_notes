# Dependencies
from aurora import Controller, View
from aurora.security import redirect, check_session, check_cookie, unset_session, unset_cookie

# The controller class
class Logout(Controller):

    # GET Method
    def get(self):
        # Check 'user' session
        if check_session('user'):
            unset_session('user')

        # Check 'user' cookie
        if check_cookie('user'):
            return unset_cookie(name='user', data={'type':'redirect', 'response':'/'})

        # Return to home
        return redirect(url='/')
