import app
from flask import request, jsonify
import xml_util

@app.app.route('/xml_transfer', methods=[ 'POST' ])
def xml_transfer():
    return jsonify(xml_util.parse_xml(request.data))
