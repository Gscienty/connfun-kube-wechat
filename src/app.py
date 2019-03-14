from flask import Flask, request, abort
from . import wechat_sec, xml_util, http_util, fields_require

app = Flask(__name__)

def process(uri, sec=False):
    if sec:
        res_content = http_util.security_call(uri,
                wechat_sec.req_build(request.json))
    else:
        res_content = http_util.normal_call(uri,
                wechat_sec.req_build(request.json))

    if wechat_sec.sign(res_content) != res_content['sign']:
        return {}, 510
    return req_content, 200

