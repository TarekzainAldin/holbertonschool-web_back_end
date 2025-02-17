#!/usr/bin/env python3
""" Initialize Blueprint for views """
from flask import Blueprint

# Define the blueprint once
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import all route modules AFTER defining the blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
