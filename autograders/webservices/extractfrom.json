import urllib.request
import ssl
import json
from pprint import pprint
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1905271.json'
total = 0
data = json.loads(urllib.request.urlopen(url,context=ctx).read().decode())
comments = data['comments']
for i in comments:
    total += int(i['count'])
print(total)
