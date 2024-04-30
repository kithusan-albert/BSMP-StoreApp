from flask import Flask, redirect, url_for

from .Auth import auth as auth_blueprint
from .Admin import admin as admin_blueprint
from .Customer import customer as customer_blueprint
from .Client import client as client_blueprint
from .Cart import cart as cart_blueprint
from .Store import store as store_blueprint



def create_app():
    app = Flask(__name__)
    
    # Set up app secret key
    app.secret_key = "Our group secret key is 345"

    # Registering blueprintsw
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(customer_blueprint, url_prefix='/customer')
    app.register_blueprint(client_blueprint, url_prefix='/client')
    app.register_blueprint(cart_blueprint, url_prefix='/cart')
    app.register_blueprint(store_blueprint, url_prefix='/store')

    @app.route('/')
    def index():
        return redirect(url_for('store.home'))
    
    return app