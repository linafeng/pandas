# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# datafreame
data = {'Chinese': [66, 95, 93, 90,np.nan], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df2)

def count_sum(df):
    df['sum'] = (df[u'English'] + df[u'Math']+df[u'Chinese'])
    return df


df1 = df1.apply(count_sum, axis=1, args=())
print(df1)
