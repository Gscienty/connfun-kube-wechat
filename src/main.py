from app import app
import os
import order_query

def __log_env():
    print('APP_ID: {}'.format(os.environ['APP_ID']))
    print('MCH_ID: {}'.format(os.environ['MCH_ID']))
    print('SUB_APPID: {}'.format(os.environ['SUB_APPID']))
    print('SUB_MCH_ID: {}'.format(os.environ['SUB_MCH_ID']))
    print('SUB_KEY: {}'.format(os.environ['SUB_KEY']))
    print('API_CERT: {}'.format(os.environ['API_CERT']))
    print('API_KEY: {}'.format(os.environ['API_KEY']))

if __name__ == '__main__':
    __log_env()
    app.run(host='0.0.0.0', port=5000)
