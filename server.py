'''
from flask import Flask
from flask_login import LoginManager

from Database import *
from lib.AppointmentSystem import *
from lib.search_database import *

#should also import database but idk what it does 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Another_highly_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

#this is the login stuff, uncomment when working on this
#app.secret_key = 'very-secret-123'  # Used to add entropy
#login_manager = LoginManager()
#login_manager.init_app(app)
login_manager.login_view = 'login'

#AppointmentSystem = AppointmentSystem()
warehouse = ProviderSearchData.load_data()
warehouse2 = CentreSearchData.load_data2()
'''        
from flask import Flask
from flask_login import LoginManager
from lib.UserManager import AuthenticationManager
from Database import bootstrap_system
app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy


# Authentication manager and System setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return system.get_user_by_id(user_id)
    
auth_manager = AuthenticationManager(login_manager)
system = bootstrap_system(auth_manager)
system = system.load_data(system)
#provider_system = ProviderSystem(auth_manager)




