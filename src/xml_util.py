import xml
from bs4 import BeautifulSoup
import os
import app

def to_xml(req_content):
    xml_items = []
    for k in sorted(req_content.keys()):
        v = req_content[k]
        if req_content[k] is None or req_content[k] == '':
            continue
        if k == 'detail' and not v.startswith('<![CDATA['):
            v = '<![CDATA[{}]]'.format(v)
        xml_items.append('<{key}>{value}</{key}>'.format(key=k, value=v))
    res = '<xml>{}</xml>'.format(''.join(xml_items))
    if os.environ['RUN_ENV'] in { 'mock', 'develop' }:
        app.app.logger.debug(res)
    return res

def parse_xml(xml_content):
    soup = BeautifulSoup(xml_content, features='xml')
    xml = soup.find('xml')
    if not xml:
        return {}
    res = dict([(item.name, item.text) for item in xml.find_all()])
    if os.environ['RUN_ENV'] in { 'mock', 'develop' }:
        app.app.logger.debug(res)
    return res
