from . import app, inspect

@app.app.route('/micro-pay/refund')
@inspect.fields({ [ 'transaction_id', 'out_trade_no' ], 'total_fee', 'refund_fee' })
def micro_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/jsapi/refund')
@inspect.fields({ [ 'transaction_id', 'out_trade_no' ], 'total_fee', 'refund_fee' })
def jsapi_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/native/refund')
@inspect.fields({ [ 'transaction_id', 'out_trade_no' ], 'total_fee', 'refund_fee' })
def native_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/app/refund')
@inspect.fields({ [ 'transaction_id', 'out_trade_no' ], 'total_fee', 'refund_fee' })
def app_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/h5/refund')
@inspect.fields({ [ 'transaction_id', 'out_trade_no' ], 'out_refund_no', 'total_fee', 'refund_fee' })
def h5_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

