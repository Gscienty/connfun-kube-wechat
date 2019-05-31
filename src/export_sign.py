import app, app_inspect
import wechat_sec
from flask import request, jsonify

@app.app.route('/sign', methods=[ 'POST' ])
def export_sign():
    return jsonify({ 'sign': wechat_sec.sign(request.json)})
