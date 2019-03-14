from . import xml_util
import requests
import os

__headers = { 'Content-Type': 'application/xml' }

def normal_call(uri, content):
    global __headers
    content = requests.post(uri,
            data=content,
            headers=__headers)

    res_dict = xml_util.parse_xml(content)

    return res_dict

def security_call(uri, content):
    global __headers
    content = requests.post(uri,
            data=content,
            headers=__headers,
            cert=(os.environ['API_CERT'], os.environ['API_KEY']))
