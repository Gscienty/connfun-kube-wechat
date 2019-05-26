import xml
import sys
from bs4 import BeautifulSoup

def to_xml(req_content):
    xml_items = []
    for k in sorted(req_content.keys()):
        v = req_content[k]
        if req_content[k] is None or req_content[k] == '':
            continue
        if k == 'detail' and not v.startswith('<![CDATA['):
            v = '<![CDATA[{}]]'.format(v)
        xml_items.append('<{key}>{value}</{key}>'.format(key=k, value=v))
    ret = '<xml>{}</xml>'.format(''.join(xml_items))
    print(ret, file=sys.stderr)
    return ret

def parse_xml(xml_content):
    soup = BeautifulSoup(xml_content, features='xml')
    xml = soup.find('xml')
    if not xml:
        return {}
    return dict([(item.name, item.text) for item in xml.find_all()])
