import app, app_inspect

@app.app.route('/micro-pay/authcodetopenid')
@app_inspect.fields({ 'auth_code' })
def micro_pay_auth_code_to_openid():
    return app.process('https://api.mch.weixin.qq.com/tools/authcodetoopenid')

