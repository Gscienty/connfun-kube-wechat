from . import app, inspect

@app.app.route('/micro-pay/order-query')
@inspect.fields({[ 'transaction_id', 'out_trade_no' ]})
def micro_pay_order_query():
    return app.process('https://api.mch.weixin.qq.com/pay/orderquery')

