import app, app_inspect

@app.app.route('/micro-pay/refund', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no' ), 'out_refund_no', 'total_fee', 'refund_fee' })
def micro_pay_refund():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/jsapi/refund', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no' ), 'out_refund_no', 'total_fee', 'refund_fee' })
def jsapi_pay_refund():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/native/refund', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no' ), 'out_refund_no', 'total_fee', 'refund_fee' })
def native_pay_refund():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/app/refund', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no' ), 'out_refund_no', 'total_fee', 'refund_fee' })
def app_pay_refund():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/h5/refund', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no' ), 'out_refund_no', 'total_fee', 'refund_fee' })
def h5_pay_refund():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)

@app.app.route('/micro-app/refund', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no' ), 'out_refund_no', 'total_fee', 'refund_fee' })
def micro_app_pay_refund():
    return app.process('https://api.mch.weixin.qq.com/secapi/refund', sec=True)
