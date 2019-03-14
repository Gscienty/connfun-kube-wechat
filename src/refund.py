from . import app, inspect

@app.app.route('/micro-pay/refund')
@inspect.fields({ [ 'transaction_id', 'out_trade_no' ], 'total_fee', 'refund_fee' })
def micro_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)
