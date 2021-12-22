from pydantic import BaseModel, Field
from .constants import *


class Credentials(BaseModel):
    """
    Parsing and validating requests that include user credentials
    """
    email: str = Field(
        ..., # is required
        min_length=EMAIL_MINLEN,
        max_length=EMAIL_MAXLEN,
        regex=EMAIL_REGEX
        )
    password: str = Field(
        ..., # is required
        min_length=PASS_MINLEN,
        max_length=PASS_MAXLEN,
        regex=PASS_REGEX
        )


class Bearer(BaseModel):
    Authorization: str = Field(
        ..., # is required
        min_length=BEARER_MINLEN,
        max_length=BEARER_MAXLEN,
        regex=TOKEN_REGEX
        )

class Refresh(BaseModel):
    Authorization: str = Field(
        ..., # is required
        min_length=REFRESH_MINLEN,
        max_length=REFRESH_MAXLEN,
        regex=TOKEN_REGEX
        )
