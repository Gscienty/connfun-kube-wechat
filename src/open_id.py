from flask import jsonify, request
import app, app_inspect
import requests
import os

@app.app.route('/wechat-oauth2-uri', methods=[ 'POST' ])
@app_inspect.fields({ 'scope' })
def wechat_oauth2():
    auth_params = request.json
    req_uri = 'https://open.weixin.qq.com/connect/oauth2/authorize'
    req_uri += '?appid={}'.format(os.getenv('SUB_APP_ID'))
    req_uri += '&redirect_uri={}'.format(os.getenv('OAUTH_REDIRECT_URI'))
    req_uri += '&response_type=code'
    req_uri += '&scope={}'.format(auth_params['scope'])
    req_uri += '&state={}'.format(auth_params['state'] if 'state' in auth_params else '')
    return jsonify({ 'uri': req_uri }), 200

@app.app.route('/wechat-oauth2-access', methods=[ 'POST' ])
@app_inspect.fields({ 'code' })
def wechat_access():
    req_uri = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    req_uri += '&appid={}'.format(os.getenv['SUB_APP_ID'])
    req_uri += '&secret={}'.format(os.getenv('SUB_KEY'))
    req_uri += '&code={}'.format(request.json['code'])
    req_uri += '&grant_type=authorization_code'
    res = requests.get(uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json), 200


