from app import app
import os
import auth_code_to_openid
import close_order
import micro_pay
import order_query
import refund
import refund_query
import reverse
import short_url
import unified_order
import xml_transfer

def __log_env():
    print_lambda = lambda name: '{name}: {value}'.format(name=name, value=os.environ[name]) if name in os.environ else '{name}: undefined'.format(name=name)
    print(print_lambda('APP_ID'))
    print(print_lambda('MCH_ID'))
    print(print_lambda('SUB_APP_ID'))
    print(print_lambda('SUB_MCH_ID'))
    print(print_lambda('SUB_KEY'))
    print(print_lambda('API_CERT'))
    print(print_lambda('API_KEY'))
    print(print_lambda('RUN_ENV'))

if __name__ == '__main__':
    __log_env()
    app.run(host='0.0.0.0', port=5000)
