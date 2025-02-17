from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import routes correctly
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import auth_session_login, auth_session_logout  # ✅ Import only the functions


User.load_from_file()
