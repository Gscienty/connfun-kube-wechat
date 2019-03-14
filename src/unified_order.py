from . import app, inspect

@app.app.route('/jsapi/unified-order')
@inspect.fields({ 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'notify_url', 'trade_type' })
def jsapi_unified_order():
    return app.process('https://api.mch.weixin.qq.com/pay/unifiedorder')

