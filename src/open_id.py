from flask import jsonify, request
import app, app_inspect, wechat_sec
import requests
import os

@app.app.route('/oauth2/uri', methods=[ 'POST' ])
@app_inspect.fields({ 'scope' })
def wechat_oauth2_uri():
    auth_params = request.json
    req_uri = 'https://open.weixin.qq.com/connect/oauth2/authorize'
    req_uri += '?appid={}'.format(os.getenv('SUB_APP_ID'))
    req_uri += '&redirect_uri={}'.format(wechat_sec.get_oauth_redirect_uri() if 'redirect_uri' not in auth_params else auth_params['redirect_uri'])
    req_uri += '&response_type=code'
    req_uri += '&scope={}'.format(auth_params['scope'])
    req_uri += '&state={}'.format(auth_params['state'] if 'state' in auth_params else '')
    req_uri += '#wechat_redirect'
    return jsonify({ 'uri': req_uri }), 200

@app.app.route('/oauth2/access', methods=[ 'POST' ])
@app_inspect.fields({ 'code' })
def wechat_oauth2_access():
    req_uri = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    req_uri += '?appid={}'.format(os.getenv('SUB_APP_ID'))
    req_uri += '&secret={}'.format(os.getenv('SUB_APP_SECRET'))
    req_uri += '&code={}'.format(request.json['code'])
    req_uri += '&grant_type=authorization_code'
    res = requests.get(req_uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json()), 200

@app.app.route('/oauth2/fresh', methods=[ 'POST' ])
@app_inspect.fields({ 'token' })
def wechat_oauth2_fresh():
    req_uri = 'https://api.weixin.qq.com/sns/oauth2/refresh_token'
    req_uri += '?appid={}'.format(os.getenv('SUB_APP_ID'))
    req_uri += '&grant_type=refresh_token'
    req_uri += '&refresh_token={}'.format(request.json['token'])
    res = requests.get(req_uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json()), 200

@app.app.route('/oauth2/userinfo', methods=[ 'POST' ])
@app_inspect.fields({ 'token' , 'openid' })
def wechat_oauth2_userinfo():
    req_uri = 'https://api.weixin.qq.com/sns/userinfo'
    req_uri += '?access_token={}'.format(request.json['token'])
    req_uri += '&openid={}'.format(request.json['openid'])
    req_uri += '&lang=zh_CN'
    res = requests.get(req_uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json()), 200

@app.app.route('/oauth2/verify', methods=[ 'POST' ])
@app_inspect.fields({ 'token', 'openid' })
def wechat_oauth2_verify():
    req_uri = 'https://api.weixin.qq.com/sns/auth'
    req_uri += '?access_token={}'.format(request.json['token'])
    req_uri += '&openid={}'.format(request.json['openid'])
    res = requests.get(req_uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json()), 200
