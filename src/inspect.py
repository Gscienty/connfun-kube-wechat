from flask import abort, request

def fields(con_junction):
    def __wrapper(func):
        def __inner(*args, **kwargs):
            if request.json is None:
                abort(400)
            for con in con_junction:
                if isinstance(con, str):
                    if con not in request.json:
                        abort(400)
                elif isinstance(con, list):
                    satisfy = False
                    for sub_con in con:
                        if sub_con in request.json:
                            satisfy = True
                    if satisfy == False:
                        abort(400)
                else:
                    abort(500)

            return func(*args, **kwargs)
        return __inner
    return __wrapper
