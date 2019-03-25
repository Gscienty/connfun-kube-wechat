import app, app_inspect

@app.app.route('/micro-pay/refund-query', methods=[ 'POST' ])
@app_inspect.fields({ ( 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' ) })
def micro_pay_refund_query():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/jsapi/refund-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' )})
def jsapi_pay_refund_query():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/native/refund-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' )})
def native_pay_refund_query():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/app/refund-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' )})
def app_pay_refund_query():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/h5/refund-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' )})
def h5_pay_refund_query():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

@app.app.route('/micro-app/refund-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no', 'out_refund_no', 'refund_id' )})
def micro_app_pay_refund_query():
    return app.process('https://api.mch.weixin.qq.com/api/refundquery')

