import urllib.request
import http.cookiejar

print('网页下载器')
url = "https://www.htouhui.com"
print ('第一种方法')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(response1.read())

print('第二种方法')
request = urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print (response1.getcode())
print(len(response2.read()))

print('第三种方法')
cj =http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print (cj)
print(response3.read())
