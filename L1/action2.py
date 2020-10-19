'''
Action2: 统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）

'''

# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

persontype = np.dtype({'names': ['姓名', '语文', '数学', '英语'], 'formats': ['S32', 'i', 'i', 'i']})
peoples = np.array([('zhangfei', 68, 65, 30), ('guanyu', 95, 76, 98), ('liubei', 98, 86, 88), ('dianwei', 90, 88, 77),
                    ('xuzhu', 80, 90, 90)], dtype=persontype)

# 平均成绩
print('语文平均成绩 %f' % np.mean(peoples['语文']))
print('数学平均成绩 %f' % np.mean(peoples['数学']))
print('英语平均成绩 %f' % np.mean(peoples['英语']))

# 最小成绩
print('语文最小成绩 %d' % np.min(peoples['语文']))
print('数学最小成绩 %d' % np.min(peoples['数学']))
print('英语最小成绩 %d ' % np.min(peoples['英语']))

# 最大成绩
print('语文最大成绩 %d' % np.max(peoples['语文']))
print('数学最大成绩 %d' % np.max(peoples['数学']))
print('英语最大成绩 %d' % np.max(peoples['英语']))

# 方差
print('语文方差 %f' % np.var(peoples['语文']))
print('数学方差 %f' % np.var(peoples['数学']))
print('英语方差 %f' % np.var(peoples['英语']))

# 标准差
print('语文标准差 %f' % np.std(peoples['语文']))
print('数学标准差 %f' % np.std(peoples['数学']))
print('英语标准差 %f' % np.std(peoples['英语']))

# 总成绩排名
rank = pd.DataFrame(peoples, index=peoples['姓名'], columns=['语文', '数学', '英语'])
rank['总成绩'] = rank['语文'] + rank['数学'] + rank['英语']
print('总成绩排名')
print(rank.sort_values(by='总成绩', ascending=False))
