from lxml import etree
import re
import requests
import time
from scrapy import Selector
import cv2
url_1 = 'https://manhua.fzdm.com/02/'
url_2 = '/index_'
url_3 = '.html'
nums_init = 900
nums_end = 901
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0' }
# 返回一集有多少页，防止有访问不到的页面，但是这个网站采用了js格式来打开网页
# 集体注释，ctrl + /
# def photo_nums(nums1):
#     photo_num = 0
#     url = url_1 + str(nums1) + '/' + url_2 + '/'
#     html = requests.get(url, headers=headers).content
#     selector = etree.HTML(html)
#     content = selector.xpath()
#     return photo_num
# 用异常捕捉来访问每一个网页
# if response.status_code == 200:#判断是否响应状态是否正常
# 配合try-except使用
# https://manhua.fzdm.com/02/1010/index_0.html
# https://manhua.fzdm.com/02/900/index_0.html
# https://manhua.fzdm.com/02/900/index_1.html
def haizeiwang(nums):
    url_init = url_1 + str(nums) + '/index_'
    print(url_init)
    for i in range(0, 30):
    # 因为没法知道有多少页，就用异常来捕获
        try:
            url = url_init + str(i) + '.html'
            print(url)
            html = requests.get(url, headers=headers).content
            print(html)
            selector = etree.HTML(html)
            content = selector.xpath('/html/body/div[4]')
            print(content)
            for i in content:
                img = requests.get(i, headers = headers)
                time.sleep(1)
                with open('C:\\Users\LeeJan\PycharmProjects\Tools_PyProGrams\爬虫\海贼王漫画', 'wb') as f:
                    f.write(img.content)

        except:
            break
if  __name__=="__main__":
    # for i in range(nums_init, nums_end):
    #     print(i)
    #     haizeiwang(i)
    url = 'http://www-mipengine-org.mipcdn.com/i/p3.manhuapan.com/2021/04/09221006894313.jpg'
    img = requests.get(url,headers=headers)


# with open结构打开文件，不打开文件夹
#     with open('C:\\Users\LeeJan\PycharmProjects\Tools_PyProGrams\爬虫\海贼王漫画\\1.jpg', 'wb') as f:
#         f.write(img.content)
# 此例子用来测试图片链接是否可以下载下来
