from app import app
import os
import order_query

def __log_env():
    print_lambda = lambda name: '{name}: {value}'.format(name=name, value=os.environ[name]) if name in os.environ else '{name}: undefined'.format(name=name)
    print(print_lambda('APP_ID'))
    print(print_lambda('MCH_ID'))
    print(print_lambda('SUB_APP_ID'))
    print(print_lambda('SUB_MCH_ID'))
    print(print_lambda('SUB_KEY'))
    print(print_lambda('API_CERT'))
    print(print_lambda('API_KEY'))

if __name__ == '__main__':
    __log_env()
    app.run(host='0.0.0.0', port=5000)
