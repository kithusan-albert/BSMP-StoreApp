# __init__.py indicates to Python that this directory is a module.
# This module handles operations of staff
from flask import Blueprint, render_template

# Create the 'Staff' Blueprint
staff = Blueprint("staff", __name__, static_folder='static', template_folder='templates')

# Import route defined within this Blueprint module.
from . import routes 

