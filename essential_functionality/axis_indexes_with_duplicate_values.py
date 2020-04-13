# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

print('重复的索引')
obj = Series(list(range(5)), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
print(obj.index.is_unique)  # 判断是否有重复索引
print(obj['a'].values)
print(obj['a'][[0]])
print(obj.a[[0]])
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'].iloc[0])
print(df.loc['b'].iloc[1])
