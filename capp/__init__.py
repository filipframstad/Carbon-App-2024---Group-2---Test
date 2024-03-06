from flask import Flask
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY'] 
# in terminal --> python --> import os --> os.urandom(24) hex() 

application.config['SECRET_KEY'] = '35b7661ed7405d6fa32ab31bdb5aaf5e2e6b17ee10a4380f' 

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

