import requests
import json
import time

url = 'https://gdgrain.com/sgtcPortals-front/sgtc/portals/SPql001'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '59',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'gdgrain.com',
    'Origin': 'https://gdgrain.com',
    'Referer': 'https://gdgrain.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
form_data = {"pageNo": 1, "pageSize": 10, "iColumnId": 5, "channelCode": "04"}  # 字典类型，需要转成json类型
resp = requests.post(url=url, data=json.dumps(form_data), headers=headers)
json_data = json.loads(resp.text)
for data in json_data['result']['orderBeanLists']:
    title = data['sTitle']
    publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data['dCreateDate']) / 1000))
    print(title, publish_time)
