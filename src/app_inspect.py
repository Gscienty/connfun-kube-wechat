from flask import request

def fields(con_junction):
    def __wrapper(func):
        def __inner(*args, **kwargs):
            if request.json is None:
                return '', 400
            for con in con_junction:
                if isinstance(con, str):
                    if con not in request.json:
                        return '', 400
                elif isinstance(con, list):
                    satisfy = False
                    for sub_con in con:
                        if sub_con in request.json:
                            satisfy = True
                    if satisfy == False:
                        return '', 400
                else:
                    return '', 500

            return func(*args, **kwargs)
        return __inner
    return __wrapper
