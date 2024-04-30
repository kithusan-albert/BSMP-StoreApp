# __init__.py indicates to Python that this directory is a module.
# Initialize a Blueprint for the 'Authentication' module.
# This module handles operations such as logins, registration, and sign-outs, etc.
from flask import Blueprint, render_template

# Create the 'auth' Blueprint with specific folder names for templates and static files.
auth = Blueprint("auth", __name__, static_folder='static', template_folder='templates')

# Import routes defined within this Blueprint module.
from . import routes
