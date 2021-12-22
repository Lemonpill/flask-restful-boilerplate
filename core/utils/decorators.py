from functools import wraps
from core import db
from flask import request, current_app
import jwt
from jwt.exceptions import PyJWTError
from pydantic.error_wrappers import ValidationError
from werkzeug.exceptions import BadRequest, Unauthorized
from core.models import User
from core.parsers import schemas


def decorator_boilerplate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = None
        return f(data, *args, **kwargs)
    return decorated

def json_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = None
        try:
            assert request.is_json
        except AssertionError:
            raise BadRequest(description="content-type must be application/json")
        try:
            data = request.get_json()
        except Exception:
            raise BadRequest(description="invalid json format")
        try:
            assert isinstance(data, dict)
        except AssertionError:
            raise BadRequest(description="invalid json format")
        return f(data, *args, **kwargs)
    return decorated

def bearer_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            assert "Authorization" in request.headers
        except AssertionError:
            raise Unauthorized
        auth_value = request.headers["Authorization"]
        try:
            token = schemas.Bearer(**{"Authorization": auth_value})
        except ValidationError:
            raise Unauthorized
        try:
            decoded = jwt.decode(
                jwt=token.Authorization[7:],
                key=current_app.secret_key,
                algorithms=["HS256"]
            )
        except PyJWTError:
            raise Unauthorized
        try:
            assert decoded["scp"] == "access"
        except AssertionError:
            raise Unauthorized
        user = db.session.query(User).filter_by(
            id=decoded["uid"],
            deleted_at=None
        ).first()
        if not user:
            raise Unauthorized
        return f(user, *args, **kwargs)
    return decorated

def bearer_optional(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # no authorization
        if "Authorization" not in request.headers:
            return f(None, *args, **kwargs)
        # bearer authorization 
        auth_value = request.headers["Authorization"]
        try:
            token = schemas.Bearer(**{"Authorization": auth_value})
        except ValidationError:
            raise Unauthorized
        try:
            decoded = jwt.decode(
                jwt=token.Authorization[7:],
                key=current_app.secret_key,
                algorithms=["HS256"]
            )
        except PyJWTError:
            raise Unauthorized
        try:
            assert decoded["scp"] == "access"
        except AssertionError:
            raise Unauthorized
        user = db.session.query(User).filter_by(
            id=decoded["uid"],
            deleted_at=None
        ).first()
        try:
            assert user
        except AssertionError:
            raise Unauthorized
        return f(user, *args, **kwargs)
    return decorated

def refresh_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            assert "Authorization" in request.headers
        except AssertionError:
            raise Unauthorized
        auth_value = request.headers["Authorization"]
        try:
            token = schemas.Refresh(**{"Authorization": auth_value})
        except ValidationError:
            raise Unauthorized
        try:
            decoded = jwt.decode(
                jwt=token.Authorization[7:],
                key=current_app.secret_key,
                algorithms=["HS256"]
            )
        except PyJWTError:
            raise Unauthorized
        try:
            assert decoded["scp"] == "refresh"
        except AssertionError:
            raise Unauthorized
        user = db.session.query(User).filter_by(
            id=decoded["uid"],
            deleted_at=None
        ).first()
        try:
            assert user
        except AssertionError:
            raise Unauthorized
        return f(user, *args, **kwargs)
    return decorated