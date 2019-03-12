from flask import Flask, request, abort
from . import wechat_sec, xml_util, http_util

wechat_pay_gateway = Flask(__name__)

@wechat_pay_gateway.route("/unifiedorder/<string:trade_type>/<string:out_trade_no>",
        methods=[ 'POST' ])
def unifiedOrder(trade_type, out_trade_no):
    uri = 'https://api.mch.weixin.qq.com/pay/unifiedorder'

    if request.json is None:
        abort(400)

    if 'body' not in request.json or 'total_fee' not in request.json:
        abort(400)

    req_content = wechat_sec.common_req_generate()
    req_content['out_trade_no'] = out_trade_no
    req_content['trade_type'] = trade_type
    for key in request.json:
        req_content[key] = request.json[key]
    req_content['sign'] = wechat_sec.sign(req_content)

    res_content = http_util.normal_call(uri, req_content)
    res_sign = wechat_sec.sign(res_content)
    if res_sign != res_content['sign']:
        return {}, 510

    return req_content, 200
