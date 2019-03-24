from flask import request, jsonify
from functools import wraps

def fields(con_junction):
    def __wrapper(func):
        @wraps(func)
        def __inner(*args, **kwargs):
            if request.json is None:
                return jsonify({ 'status': 'CHECK_FAILED', 'msg': 'request body empty' }), 400
            for con in con_junction:
                if isinstance(con, str):
                    if con not in request.json:
                        print("FUCK HERE")
                        return jsonify({ 'status': 'CHECK_FAILED', 'msg': 'lack required field' }), 400
                elif isinstance(con, tuple):
                    satisfy = False
                    for sub_con in con:
                        if sub_con in request.json:
                            satisfy = True
                    if satisfy == False:
                        print("FUCK HERE")
                        return jsonify({ 'status': 'CHECK_FAILED', 'msg': 'lack required field' }), 400
                else:
                    return jsonify({ 'status': 'SERVER_FAILED', 'msg': 'inner error' }), 500
            return func(*args, **kwargs)
        return __inner
    return __wrapper
