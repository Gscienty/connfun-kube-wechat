from flask import Flask, request, abort, jsonify
import wechat_sec, http_util
import os

app = Flask(__name__)

def process(uri, sec=False):
    run_env = os.environ['RUN_ENV']
    req = wechat_sec.req_build(request.json)
    if run_env in { 'develop', 'mock' }:
        app.logger.debug('client request: uri: {uri};sec:{sec}; req body: {req}'.format(uri=uri, sec=sec, req=str(req)))
    if sec:
        res_content = http_util.security_call(uri, req)
    else:
        res_content = http_util.normal_call(uri, req)

    if 'sign' not in res_content:
        return jsonify(res_content), 400
    if wechat_sec.sign(res_content) != res_content['sign']:
        return {}, 510
    return jsonify(res_content), 200

