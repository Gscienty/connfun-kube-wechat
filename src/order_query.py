import app, app_inspect

@app.app.route('/micro-pay/order-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no' )})
def micro_pay_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')

@app.app.route('/jsapi/order-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no' )})
def jsapi_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')

@app.app.route('/native/order-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no' )})
def native_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')

@app.app.route('/app/order-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no' )})
def app_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')

@app.app.route('/h5/order-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no' )})
def h5_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')

@app.app.route('/micro-app/order-query', methods=[ 'POST' ])
@app_inspect.fields({( 'transaction_id', 'out_trade_no' )})
def micro_app_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')
