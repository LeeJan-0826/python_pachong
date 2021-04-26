import os
import requests
from lxml import etree
import time
url_1 = 'http://www.566xsw.com/xinhun/'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
# 这里换成了text,而不是content。有结果
html = requests.get(url_1, headers=headers).text
# print(html)
selector = etree.HTML(html)
content = selector.xpath('//*[@id="list"]/dl//@href')
# 获取//*[@id="list"]/dl下 "href"的属性
# print(content)
def prsase_url(url):
    #print(url)
    html = requests.get(url, headers=headers).text
    # print(html)
    selector = etree.HTML(html)
    #print(selector)
    # content = selector.xpath('/html/body/div/div/div/div[3]/text')
    content = selector.xpath('//*[@id="content"]//text()')
    print(content.encode('utf-8'))
    #content内部是一种无法写入txt文件的格式，需要进行类型转换
    print(type(content[0]))
    with open('新婚.txt','wb') as f:
        for i in content:
            f.write(i.decode())
    time.sleep(10)
for i in content:
    url = url_1 + i
    prsase_url(url)

