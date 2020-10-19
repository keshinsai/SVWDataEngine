import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求URL
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=10)
content = html.text
# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')


table_heads = ['id', 'brand', 'car_model', 'type', 'description', 'problem', 'datetime', 'status']
df = pd.DataFrame(colums=table_heads)

# 获得表格内容
    table = soup.find('div', class_='tslb_b')
    # 获取表格所有tr标签
    tr_list = table.find_all('tr')
    for tr in tr_list:
        # 获取每行信息
        td_list = tr.find_all('td')
        # print(td_list)
        # 用于保存每行结果的字典
        item = {}
        # if len(td_list) > 0:
        for i in range(len(td_list)):
            item[table_heads[i]] = td_list[i].text
        df = df.append(item, ignore_index=True)
    df.drop(0, axis=0, inplace=True)

