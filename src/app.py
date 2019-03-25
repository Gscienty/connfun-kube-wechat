from flask import Flask, request, abort, jsonify
import wechat_sec, http_util

app = Flask(__name__)

def process(uri, sec=False):
    if sec:
        res_content = http_util.security_call(uri,
                wechat_sec.req_build(request.json))
    else:
        res_content = http_util.normal_call(uri,
                wechat_sec.req_build(request.json))

    if 'sign' not in res_content:
        return jsonify(res_content), 400
    if wechat_sec.sign(res_content) != res_content['sign']:
        return {}, 510
    return jsonify(res_content), 200

