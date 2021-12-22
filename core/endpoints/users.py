from flask import Blueprint
from werkzeug.exceptions import Unauthorized
from core.models import User
from core.utils.decorators import bearer_required

users = Blueprint(name="users", import_name=__name__)

@users.route("<int:user_id>", methods=["GET"])
def user_info(user_id):
    return {"route": "get user info"}

@users.route("<int:user_id>", methods=["PATCH"])
@bearer_required
def update_user(current_user, user_id):
    return {"route": "update user info"}
