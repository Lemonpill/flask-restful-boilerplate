import jwt
from datetime import datetime, timedelta
from flask import Blueprint, current_app
from pydantic.error_wrappers import ValidationError
from werkzeug.exceptions import BadRequest, Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash
from core.utils.decorators import json_required, refresh_required
from core.parsers import schemas, helpers
from core.models import User
from core import db


auth = Blueprint(name="auth", import_name=__name__)


@auth.route("register", methods=["POST"])
@json_required
def create_user(request_body):
    try:
        data = schemas.Credentials(**request_body)
    except ValidationError as e:
        errors = helpers.errors_to_dict(e.errors)
        return errors, 400, {"X-Validation-Error": "validation failed"}
    user = db.session.query(User).filter_by(email=data.email).first()
    if user:
        raise BadRequest("email exists")
    new_user = User(
        email=data.email,
        password=generate_password_hash(data.password, "SHA256"),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()
    return {
        "id":new_user.id,
        "email": new_user.email,
        "created": new_user.created_at,
        "updated": new_user.updated_at
    }, 201

@auth.route("token", methods=["POST"])
@json_required
def token(request_body):
    try:
        data = schemas.Credentials(**request_body)
    except ValidationError:
        raise Unauthorized
    user = db.session.query(User).filter_by(email=data.email).first()
    if not user:
        raise Unauthorized
    if not check_password_hash(user.password, data.password):
        raise Unauthorized
    bearer = jwt.encode(
        payload={
            "uid": user.id,
            "exp": datetime.now() + timedelta(minutes=15),
            "scp": "access"
        },
        key=current_app.secret_key
    )
    refresh = jwt.encode(
        payload={
            "uid": user.id,
            "exp": datetime.now() + timedelta(hours=3),
            "scp": "refresh"
        },
        key=current_app.secret_key
    )
    return {
        "token": bearer,
        "refresh": refresh
    }, 201


@auth.route("token/refresh", methods=["POST"])
@refresh_required
def refresh_token(user):
    bearer = jwt.encode(
        payload={
            "uid": user.id,
            "exp": datetime.now() + timedelta(minutes=15),
            "scp": "access"
        },
        key=current_app.secret_key
    )
    return {
        "token": bearer,
    }, 201
    