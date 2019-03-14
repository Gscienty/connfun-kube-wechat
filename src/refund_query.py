from . import app, inspect

@app.app.route('/micro-pay/refund-query')
@inspect.fields({ [ 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ]})
def micro_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')
