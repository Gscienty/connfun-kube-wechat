from . import app, inspect

@app.app.route('/jsapi/close-order')
@inspect.fields({ 'out_trade_no' })
def jsapi_close_order():
    return app.process('https://api.mch.weixin.qq.com/pay/closeorder')

@app.app.route('/native/close-order')
@inspect.fields({ 'out_trade_no' })
def native_close_order():
    return app.process('https://api.mch.weixin.qq.com/pay/closeorder')

@app.app.route('/app/close-order')
@inspect.fields({ 'out_trade_no' })
def app_close_order():
    return app.process('https://api.mch.weixin.qq.com/pay/closeorder')

@app.app.route('/h5/close-order')
@inspect.fields({ 'out_trade_no' })
def h5_close_order():
    return app.process('https://api.mch.weixin.qq.com/pay/closeorder')

