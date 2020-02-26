'''
from lib.User import *

class UserManager:
    def __init__(self):
        self._patient = []
        self._provider = []
    
    def add_patient(self, user):
        self._patients.append(user)
    
    def add_provider(self, user):
        self._provider.append(user)

    def validate_login(self, email, password):
        user = self._patient.get(email)
        if user is None:
            return None
        return user if User.validate_password(password) else None
    
    def find_by_id(self, id):
        for i in self._patient: #search through dictionary 'patient' 
            if i.get_id() == id:
                return i
        # Not necessary but explicit
        return None
'''
from flask_login import current_user, login_required, login_user, logout_user
from flask import redirect, url_for
from functools import wraps


'''
    Wraps around flask-login's LoginManager
    to provide additional functionalities
'''
class AuthenticationManager():
    
    def __init__(self, login_manager):
        self._login_manager = login_manager
        self._default_page = 'home'

    # Try to login given user with given username and password
    def login(self, user, email, password):
        if user.email == email and user.validate_password(password):
            login_user(user) # provided by flask-login
            return user
        return None

    def logout(self):
        logout_user()

    # Redirect user to default page
    def _to_default_page(self):
        return redirect(url_for(self._default_page))
