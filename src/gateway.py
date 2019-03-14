from flask import Flask, request, abort
from . import wechat_sec, xml_util, http_util, fields_require

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


"""
统一下单
"""
@wechat_pay_gateway.route('/unifiedorder', methods=[ 'POST' ])
@fields_require.required({
    'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type'
})
def unified_order():
    return __process('https://api.mch.weixin.qq.com/pay/unifiedorder')

"""
提交付费码支付
"""
@wechat_pay_gateway.route('/micropay', methods=[ 'POST' ])
@fields_require.required({
    'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'auth_code'
}):
def micro_pay():
    return __process('https://api.mch.weixin.qq.com/pay/micropay')

"""
订单查询
"""
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


if __name__ == '__main__':
    wechat_pay_gateway.run(host='0.0.0.0', port=5000)
