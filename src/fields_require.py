from flask import abort, request

def __any_satisfy_fields(required_fields):
    if request.json is None:
        return False
    for field in required_fields:
        if isinstance(field, list):
            for sub_field in field:
                if field in request.json:
                    break
            return False
        elif field not in request.json:
            return False
    return True

def required(fields):
    def __wrapper(func):
        def __args_wrapper(*args, **kwargs):
            if __satisfy_fields(fields):
                return func(*args, **kwargs)
            else:
                abort(400)
        return __args_wrapper
    return __wrapper
