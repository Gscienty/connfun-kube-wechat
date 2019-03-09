import os
from flask import Flask, request, abort
from . import wechat_sec

wechat_pay_gateway = Flask(__name__)

@wechat_pay_gateway.route("/unifiedorder/<string:trade_type>/<string:out_trade_no>",
        methods=[ 'POST' ])
def unifiedOrder(trade_type, out_trade_no):
    uri = 'https://api.mch.weixin.qq.com/pay/unifiedorder'

    if request.json is None:
        abort(400)

    if 'body' not in request.json or 'total_fee' not in request.json:
        abort(400)

    req_content = {
            'appid': os.environ['APP_ID'],
            'mch_id': os.environ['MCH_ID'],
            'sub_appid': os.environ['SUB_APPID'],
            'sub_mch_id': os.environ['SUB_MCH_ID'],
            'nonce_str': wechat_sec.nonce_generate(),
            'body': request.json['body'],
            'detail': request.json['detail'] if 'detail' in request.json else '',
            'attach': request.json['attach'] if 'attach' in request.json else '',
            'out_trade_no': out_trade_no,
            'total_fee': request.json['total_fee'],
            'spbill_create_ip': os.environ['SPBILL_CREATE_IP'],
            'notify_url': os.environ['NOTIFY_URL'],
            'trade_type': trade_type,
            'receipt': request.json['receipt'] if 'receipt' in request.json else ''
            }
    req_content['sign'] = wechat_sec.sign(req_content)

    return ''
