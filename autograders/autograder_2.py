import requests
from bs4 import BeautifulSoup
import urllib
url = 'http://py4e-data.dr-chuck.net/comments_1905268.html'
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
t = soup.find_all('span', class_='comments')
sum_ = 0
for i in t:
    sum_ += int(i.text)
print(sum_)
