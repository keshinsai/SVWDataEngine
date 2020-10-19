'''
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多

'''

import numpy as np
import pandas as pd

# Step1 数据加载
result = pd.read_csv('car_complain.csv', encoding='utf-8')
result['brand'].replace("一汽-大众", "一汽大众", inplace=True)
print('Step1 数据加载')
print(result)

# Step2 数据预处理
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
# print(result.columns)
# tags = result.columns[7:]
print('Step2 数据预处理')
print(result)

# Step3 数据统计
# 品牌投诉总数排名
band_complaint = result.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉总数排名')
print(band_complaint.sort_values('count', ascending=False))

# 车型投诉总数排名
model_complaint = result.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉总数排名')
print(model_complaint.sort_values('count', ascending=False))

# 品牌下的平均车型投诉排名
avg_complaint = result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean()
print('品牌下的平均车型投诉排名')
print(avg_complaint.sort_values('count', ascending=False))
# file = open('result.txt','w')
# file.write(str(avg_complaint.sort_values('count', ascending=False)))
# file.close()
