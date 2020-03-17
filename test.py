import requests
import re

# 获取网页源代码
url = input("请输入b站的url(前几p)：\n\a")
url_proc = url[:-1]+"{}"
kv = {'user-agent': 'Mozilla/5.0'}       # 请求头信息，相当于一个浏览器面具
html = requests.get(url, headers=kv)
html_doc = html.text

pattern2 = re.compile(r'"page":(.*?),"from"', re.S)
item_list2 = pattern2.findall(html_doc)

# 打印页数
n = int(item_list2[-1])
print("一共{}P".format(n))

a = dict()
for num in range(1, n+1):
    url = url_proc.format(num)
    kv = {'user-agent': 'Mozilla/5.0'}  # 请求头信息，相当于一个浏览器面具
    html = requests.get(url, headers=kv)
    html_doc = html.text

    pattern = re.compile(r'"timelength":(.*?),"accept_format"', re.S)
    item_list = pattern.findall(html_doc)

    pattern_des = re.compile(r'"page":{},"from":"vupload","part":(.*?),"duration"'.format(num), re.S)
    item_list_des = pattern_des.findall(html_doc)

    # 描述
    desc = str(num) + ':' +str(item_list_des[0])

    # 时间
    time = int(item_list[0])//60000
    a[desc] = time


for k,v in a.items():
    print("P{} \t\t\t :{}分钟\n".format(k,v))