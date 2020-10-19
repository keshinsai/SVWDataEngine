'''
Action1：求2+4+6+8+...+100的求和，用Python该如何写
'''

import numpy as np

l = [i for i in range(2, 101, 2)]
print('求和 %d' %sum(l))

total = np.arange(2, 101, 2)
print('numpy sum %d' %total.sum())
