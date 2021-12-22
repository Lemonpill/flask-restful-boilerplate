# FUNCTIONS #
def errors_to_dict(errs):
    errors = dict()
    for e in errs:
        errors[e["loc"][0]] = e["msg"]
    return errors