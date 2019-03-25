import random
import os
import hashlib
from flask import request

__alpha__ = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
        'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
        'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

def nonce_generate():
    rand = random.Random()
    ret = ''
    for i in range(32):
        ret += __alpha__[rand.randint(0, len(__alpha__) - 1)]
    return ret

def sign(req_content):
    string_a_items = []
    for key in sorted(req_content.keys()):
        if key == 'sign':
            continue
        if req_content[key] is not None or req_content[key] != '':
            continue
        string_a_items.append(
                '{key}={value}'.format(key=key, value=req_content[key]))
    sub_key = request.headers.get('Sub-Key')
    if sub_key is None:
        sub_key = os.environ['SUB_KEY']
    val = '&'.join(string_a_items) + '&key=' + sub_key
    return hashlib.md5(val.encode(encoding='UTF-8')).hexdigest().upper()

def get_sub_app_id():
    return os.environ['SUB_APP_ID'] if 'Sub-Appid' not in request.headers else request.headers.get('Sub-Appid')

def get_sub_mch_id():
    return os.environ['SUB_MCH_ID'] if 'Sub-Mch-Id' not in request.headers else request.headers.get('Sub-Mch-Id')

def req_build(json_content):
    req_content = {
            'appid': os.environ['APP_ID'],
            'mch_id': os.environ['MCH_ID'],
            'sub_appid': get_sub_app_id(),
            'sub_mch_id': get_sub_mch_id(),
            'nonce_str': nonce_generate()
            }
    for pair in json_content.items():
        if pair[1] is not None:
            req_content[pair[0]] = pair[1]
    req_content['sign'] = sign(req_content)
    return req_content

def mock_res_build():
    res_content = {
            'appid': os.environ['APP_ID'],
            'mch_id': os.environ['MCH_ID'],
            'sub_appid': get_sub_app_id(),
            'sub_mch_id': get_sub_mch_id(),
            'nonce_str': nonce_generate()
            }
    for mock_header in request.headers:
        if mock_header[0].startswith('MOCK_'):
            res_content[mock_header[0][5:]] = mock_header[1]
    res_content['sign'] = sign(res_content)
    return res_content
