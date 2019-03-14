from . import app, inspect

@app.app.route('/jsapi/close-order')
@inspect.fields({ 'out_trade_no' })
def jsapi_close_order():
    return app.process('https://api.mch.weixin.qq.com/pay/closeorder')

@app.app.route('/native/close-order')
@inspect.fields({ 'out_trade_no' })
def native_close_order():
    return app.process('https://api.mch.weixin.qq.com/pay/closeorder')

