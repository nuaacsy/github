import pandas as pd
import numpy as np


df_sheet=pd.read_excel("20190925//test.xlsx")
s=df_sheet.loc[1,['学号']]
listi=[]
for i in range(len(df_sheet)):
    listi.append('a')
    print(df_sheet.iloc[0,1])
print('list i:')
print(type(i))
print(listi)