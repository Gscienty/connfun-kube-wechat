import app, app_inspect

@app.app.route('/micro-pay')
@app_inspect.fields({ 'body', 'out_trade_no', 'total_fee', 'spbill_create_ip', 'auth_code' })
def micro_pay():
    return app.process('https://api.mch.weixin.qq.com/pay/micropay')

