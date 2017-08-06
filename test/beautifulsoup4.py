import urllib.request

from bs4 import BeautifulSoup

import re;

print('网页解析器')
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

url = "https://www.htouhui.com"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(
    response.read(),
    'html.parser'
)

print('获取所有的链接a')
links = soup.find_all('a')
for link in links :
    print(link.name,link['href'],link.get_text())

print('获取elsie,lacie的链接a')
a = soup.find('a',href="http://example.com/lacie")
b = soup.find('a',href="http://example.com/elsie",class_="sister")
print(a.name,a['href'],a.get_text())
print(b.name,b['href'],b.get_text())

print('正则匹配')
re = soup.find('a',href=re.compile(r'ill'))
print(re.name,re['href'],re.get_text())