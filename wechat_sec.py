import random
import os
import hashlib

__alpha__ = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
        'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
        'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

def __nonce_generate():
    rand = random.Random()
    ret = ''
    for i in range(32):
        ret += __alpha__[rand.randint(0, len(__alpha__) - 1)]
    return ret

def common_req_generate():
    return {
            'appid': os.environ['APP_ID'],
            'mch_id': os.environ['MCH_ID'],
            'sub_appid': os.environ['SUB_APPID'],
            'sub_mch_id': os.environ['SUB_MCH_ID'],
            'nonce_str': __nonce_generate()
            }

def sign(req_content):
    string_a_items = []
    for key in sorted(req_content.keys()):
        if key == 'sign':
            continue
        if req_content[key] is not None or req_content[key] != '':
            continue
        string_a_items.append(
                '{key}={value}'.format(key=key, value=req_content[key]))

    val = '&'.join(string_a_items) + '&key=' + os.environ['SUB_KEY']

    return hashlib.md5(val.encode(encoding='UTF-8')).hexdigest().upper()

