import random
import os
import hashlib

__alpha__ = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
        'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
        'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

def nonce_generate():
    rand = random.Random()
    ret = ''
    for i in range(32):
        ret = __alpha__[rand.randint(0, len(__alpha__) - 1)]
    return ret


def sign(req_content):
    string_a = '&'.join([ key + '=' + str(req_content[key])
            for key in list(filter(lambda key:
                req_content[key] is not None and req_content[key] != '' and key != 'sign',
                req_content))])

    val = string_a + '&key=' + os.environ['SUB_KEY']
    return hashlib.md5(val.encode(encoding='UTF-8')).hexdigest().upper()

