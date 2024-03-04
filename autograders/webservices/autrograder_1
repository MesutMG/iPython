import urllib.request
import xml.etree.ElementTree as ET
import ssl
from pprint import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1905270.xml'
data = urllib.request.urlopen(url, context=ctx).read().decode()

tree = ET.fromstring(data)
comments = tree.findall('comments/comment')

total = 0
for comment in comments:
    count = int(comment.find('count').text)
    total += count

print(total)
