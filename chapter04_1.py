import requests
import re
import time

f = open('/Users/ale/workspace/scrapy_chapter01/content.txt', 'a+')  # 新建TXT文档
i = 0


def get_info(url):
    res = requests.get(url)
    print(res)
    # response.text返回的是Unicode格式，通常需要转换为utf-8格式，否则就是乱码。
    # response.content是二进制模式，可以下载视频之类的，如果想看的话需要decode成utf-8格式。
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)<p>', res.content.decode('utf-8'), re.S)
        for content in contents:
            f.write(content + '\n')
    else:
        pass


if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2, 10)]
    print(len(urls))
    for url in urls:
        get_info(url)
        i = i + 1
        time.sleep(1)
    f.close()
