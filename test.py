import requests
import re
import time


#f = open('E:/new tecinoly/py_scrapy/content.txt', 'a+')#新建TXT文档
# i=0
urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,10)]
print(urls)
for url in urls:
    res = requests.get(url)
    print(res)


