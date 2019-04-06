from flask import jsonify, request
import app, app_inspect, wechat_sec
import requests
import os

@app.app.route('/oauth2/uri', methods=[ 'POST' ])
@app_inspect.fields({ 'scope' })
def wechat_oauth2_uri():
    auth_params = request.json
    req_uri = 'https://open.weixin.qq.com/connect/oauth2/authorize'
    req_uri += '?appid={}'.format(wechat_sec.get_sub_app_id())
    req_uri += '&redirect_uri={}'.format(os.getenv('OAUTH_REDIRECT_URI'))
    req_uri += '&response_type=code'
    req_uri += '&scope={}'.format(auth_params['scope'])
    req_uri += '&state={}'.format(auth_params['state'] if 'state' in auth_params else '')
    return jsonify({ 'uri': req_uri }), 200

@app.app.route('/oauth2/access', methods=[ 'POST' ])
@app_inspect.fields({ 'code' })
def wechat_oauth2_access():
    req_uri = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    req_uri += '&appid={}'.format(wechat_sec.get_sub_app_id())
    req_uri += '&secret={}'.format(os.getenv('SUB_KEY'))
    req_uri += '&code={}'.format(request.json['code'])
    req_uri += '&grant_type=authorization_code'
    res = requests.get(uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json), 200

@app.app.route('/oauth2/fresh', methods=[ 'POST' ])
@app_inspect.fields({ 'token' })
def wechat_oauth2_fresh():
    req_uri = 'https://api.weixin.qq.com/sns/oauth2/refresh_token'
    req_uri += '?appid={}'.format(wechat_sec.get_sub_app_id())
    req_uri += '&grant_type=refresh_token'
    req_uri += '&refresh_token={}'.format(request.json['token'])
    res = requests.get(uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json), 200

@app.app.route('/oauth2/userinfo', methods=[ 'POST' ])
@app_inspect.fields({ 'token' , 'openid' })
defe wechat_oauth2_userinfo():
    req_uri = 'https://api.weixin.qq.com/sns/userinfo'
    req_uri = '&access_token={}'.format(request.json['token'])
    req_uri = '&openid={}'.format(requests.json['openid'])
    req_uri = '&lang=zh_CN'
    res = requests.get(uri,
            headers={ 'Content-Type': 'application/json' })
    return jsonify(res.json), 200

