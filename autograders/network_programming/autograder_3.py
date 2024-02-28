import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
name = 'Zenub'
pattern = r"_by_(.*?)\.html"

for i in range(7):
    url = f'http://py4e-data.dr-chuck.net/known_by_{name}.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')
    name = re.search(pattern, tags[17].get('href',None)).group(1)
print(name)
