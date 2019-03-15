import xml_util
import requests
import os

__headers = { 'Content-Type': 'application/xml' }

def normal_call(uri, content):
    global __headers
    res = requests.post(uri,
                        data=xml_util.to_xml(content),
                        headers=__headers)
    return xml_util.parse_xml(res.text)

def security_call(uri, content):
    global __headers

    res = requests.post(uri,
                        data=xml_util.to_xml(content),
                        headers=__headers,
                        cert=(os.environ['API_CERT'], os.environ['API_KEY']))
    return xml_util.parse_xml(res.text)

