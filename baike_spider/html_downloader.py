import urllib

#html下载器
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        #print(str(response.read(),'utf-8'))
        return str(response.read(),'utf-8')