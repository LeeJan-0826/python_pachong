# # 失败告终
# import requests
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
# }
# params = {
#     'kw': '小视频',
#     'page': '2',
#     'pageSize':'20',
#     'filterType': '0',
#     'tabType': '1'
# }
# print(1)
# response = requests.get(url='https://www.douyu.com/search/?kw=%E5%B0%8F%E8%A7%86%E9%A2%91',headers=headers,params=params)
# print(response.status_code)
# json_data = response.json()
# print(response.status_code)
# print(json_data)

# 复制的代码可以跑
import requests
import json
#直接找到json格式的地址，修改最后的尾数1,2,3,4
urls = ['https://www.douyu.com/gapi/rkc/directory/2_1/{}'.format(page) for page in range(1, 5)]
print(urls)
for url in urls:
    res = requests.get(url)
    j = json.loads(res.text)
    l1 = j['data']     # 通过观察可以发现要的数据在data下
    l2 = l1['rl']     #在观察发现在data的rl中
    # 正则表达式，用后面的4个参数依次代替tplt
    tplt = '{0:{4}<20}\t{1:<12}\t{2:{4}<25}\t{3:<12}'
    print(tplt)
    # print(tplt.format('主播', '房间号', '房间名', '热度', chr(12288)))

    for i in range(len(l2)):   # 这里用到for循环来处理一个列表下多个字典的数据
        Anchor = l2[i]['nn']              # 获取主播名字
        RoomNumber = l2[i]['rid']         # 获取房间号
        Heat = l2[i]['ol']                # 获取热度
        RoomName = l2[i]['rn']            # 获取房间名
        print(tplt.format(Anchor, RoomNumber, RoomName, Heat, chr(12288)))

        # 此方法适用于那些不用params的网页
        # 且已经找不到urls这个地址了