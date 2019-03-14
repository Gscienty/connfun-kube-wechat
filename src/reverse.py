from . import app, inspect

@app.app.route('/micro-pay/reverse')
@inspect.fields({[ 'out_trade_no', 'transaction_id' ]})
def micro_pay_reverse():
    return app.process('https://api.mch.weixin.qq.com/secapi/reverse', sec=True)
