from werkzeug.exceptions import HTTPException
from flask import json, request
from .messages import General
from core import log


def http(e: HTTPException):
    response = e.get_response()
    response.content_type = "application/json"
    match e.code:
        case 400:  # bad request
            msg = e.description
        case 401:  # authentication error
            msg = General.unauthorized
        case 403:  # not authorized
            msg = General.forbidden
        case 404:  # resource not found
            msg = General.not_found
        case 405:  # method not allowed
            msg = General.not_allowed
        case 429:  # too many requests
            msg = General.too_many
        case _:  # other exceptions
            msg = General.internal
            log.write(f"{request.method} {request.base_url} {request.get_data()}")
    response.data = json.dumps({"message": msg})
    return response