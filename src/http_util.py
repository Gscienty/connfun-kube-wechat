import xml_util
import requests
import os
import wechat_sec

__headers = { 'Content-Type': 'application/xml' }

def normal_call(uri, content):
    global __headers
    res = requests.post(uri,
                        data=xml_util.to_xml(content),
                        headers=__headers)
    return xml_util.parse_xml(res.text)

def security_call(uri, content):
    global __headers
    if os.environ['RUN_ENV'] in { 'release', 'develop' }:
        res = requests.post(uri,
                data=xml_util.to_xml(content),
                headers=__headers,
                cert=(os.environ['API_CERT'], os.environ['API_KEY']))
        return xml_util.parse_xml(res.text)
    elif os.environ['RUN_ENV'] in { 'mock' }:
        return wechat_sec.mock_res_build()
