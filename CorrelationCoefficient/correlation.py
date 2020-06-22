#coding:utf-8
#データの読み込み
import numpy as np
import pandas as pd

print('start')
df_score = pd.read_csv("test.csv",index_col="番号")


df_corr = df_corr = df_score.corr()
print(df_corr)
print(df_corr)