from flask import Flask, request, abort
from . import wechat_sec, xml_util, http_util

wechat_pay_gateway = Flask(__name__)

def __process(uri, sec=False):
    if sec:
        res_content = http_util.security_call(uri,
                wechat_sec.req_build(request.json))
    else:
        res_content = http_util.normal_call(uri,
                wechat_sec.req_build(request.json))

    if wechat_sec.sign(res_content) != res_content['sign']:
        return {}, 510
    return req_content, 200

def __satisfy_fields(required_fields):
    if request.json is None:
        return False
    for field in required_fields:
        if field not in request.json:
            return False
    return True

@wechat_pay_gateway.route('/<string:pay_type>/unifiedorder', methods=[ 'POST' ])
def unified_order(pay_type):
    if not __satisfy_fields({
        'body', 'out_trade_no', 'total_fee',
        'spbill_create_ip', 'notify_url', 'trade_type' }):
        abort(400)
    if pay_type == 'H5' and not __satisfy_fields({ 'scene_info' }):
        abort(400)
    return __process('https://api.mch.weixin.qq.com/pay/unifiedorder')

@wechat_pay_gateway.route('/micropay', methods=[ 'POST' ])
def micro_pay():
    if not __satisfy_fields({
        'body', 'out_trade_no', 'total_fee',
        'spbill_create_ip', 'auth_code' }):
        abort(400)
    return __process('https://api.mch.weixin.qq.com/pay/micropay')

@wechat_pay_gateway.route('/orderquery', methods=[ 'POST' ])
def order_query():
    if not __satisfy_fields({ 'transaction_id' })
    and not __satisfy_fields({ 'out_trade_no' }):
        abort(400)
    retrun __process('https://api.mch.weixin.qq.com/pay/orderquery')

@wechat_pay_gateway.route('/closeorder', methods=[ 'POST' ])
def close_order():
    retrun __process('https://api.mch.weixin.qq.com/pay/closeorder')

@wechat_pay_gateway.route('/refund', methods=[ 'POST' ])
def refund():
    retrun __process('https://api.mch.weixin.qq.com/secpay/refund', sec=True)

@wechat_pay_gateway.route('/refundquery', methods=[ 'POST' ])
def refund_query():
    retrun __process('https://api.mch.weixin.qq.com/pay/refundquery', sec=True)

