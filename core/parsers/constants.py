
EMAIL_MINLEN = 7
EMAIL_MAXLEN = 100
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

PASS_MINLEN = 8
PASS_MAXLEN = 1024
PASS_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&]).*$"

BEARER_MINLEN = 143
BEARER_MAXLEN = 143

REFRESH_MINLEN = 144
REFRESH_MAXLEN = 144

TOKEN_REGEX = r"^(Bearer [\w-]*\.[\w-]*\.[\w-]*$)"
