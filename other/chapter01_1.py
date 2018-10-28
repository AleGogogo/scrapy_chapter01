import requests
import re
from bs4 import BeautifulSoup

res = requests.get("http://bj.xiaozhu.com/")
#print(type(res))
print(res.text)
prices =re.findall('<span class="result_price">&#165;<i>(.*?)</i>起/晚</span>', res.text)
soup = BeautifulSoup(res.text,"html.parser")
print(prices)
for price in prices:
    print(price)

#price=soup.select("body>div.city_wrap>div.clearfix>div.search_box>div#page_list > ul.pic_list.clearfix> li > div.result_btm_con.lodgeunitname > span.result_price>i")

#print(price)
