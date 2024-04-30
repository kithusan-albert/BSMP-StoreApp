# __init__.py indicates to Python that this directory is a module.
# This module handles operations for business client
from flask import Blueprint, render_template

# Create the 'Client' Blueprint
# folders names for templates and static files.
# The 'static_folder' specifies the folder for static files (images)
# The 'template_folder' specifies the folder for HTML template files.
client = Blueprint("client", __name__, static_folder='static', template_folder='templates')

# Import route defined within this Blueprint module.
from . import routes 
