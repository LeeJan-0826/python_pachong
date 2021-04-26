# 导入requests库
import requests

# 导入re正则表达式库
import re

# 导入系统内置库
import os

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

# 用request.get方法访问网址得到网页HTML内容
response = requests.get('https://www.vmgirls.com/12985.html', headers = headers)

#网页内容以文本形式打印出来
html = response.text

print(html)

#为文件夹起名字用图片的名字命名。
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]

print(dir_name)

# 如果文件夹不存在那么就建立文件夹，不然就不建立
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

 # 获取图片地址
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)

# 打印获得的urls
print(urls)



# 通过for循环来遍历筛选过的urls，然后分别下载保存！
for url in urls:
    file_name = url.split('/')[-1]
    response = requests.get(url, headers = headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
