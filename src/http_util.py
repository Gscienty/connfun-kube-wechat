import xml_util
import requests
import os
import wechat_sec

__headers = { 'Content-Type': 'application/xml' }

def normal_call(uri, content):
    global __headers
    run_env = os.getenv('RUN_ENV')
    if run_env in { 'release', 'develop' }:
        res = requests.post(uri,
                data=xml_util.to_xml(content),
                headers=__headers)
        return xml_util.parse_xml(res.text)
    elif run_env in { 'mock' }:
        print(xml_util.to_xml(content))
        return wechat_sec.mock_res_build()

def security_call(uri, content):
    global __headers
    run_env = os.getenv('RUN_ENV')
    if run_env in { 'release', 'develop' }:
        res = requests.post(uri,
                data=xml_util.to_xml(content),
                headers=__headers,
                cert=(os.getenv('API_CERT'), os.getenv('API_KEY')))
        return xml_util.parse_xml(res.text)
    elif run_env in { 'mock' }:
        print(xml_util.to_xml(content))
        return wechat_sec.mock_res_build()
