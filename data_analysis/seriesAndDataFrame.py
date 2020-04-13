# -*- coding: utf-8 -*-

import pandas as pd
import openpyxl
from pandas import Series, DataFrame

# datafreame
data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)

df2 = df2.drop(columns=['Math'])
df2 = df2.drop(index=['ZhangFei'])
print(df2)

df2.rename(columns={'English': 'Yingyu'}, inplace=True)
print(df2)

df2['Chinese'].astype('str')
print(df2)
# 删除左右两边空格
df2['Chinese'] = df2['Chinese'].astype('str').map(str.strip)
print(df2)
# 删除左边空格
df2['Chinese'] = df2['Chinese'].astype('str').map(str.lstrip)
print(df2)
# 删除右边空格
df2['Chinese'] = df2['Chinese'].astype('str').map(str.rstrip)
print(df2)

# 导入导出数据
print("导入导出数据")
score = DataFrame(pd.read_excel('data.xlsx'))
score.to_excel('data1.xlsx')
print(score)

# sql操作pandas
import pandas as pd
from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))
