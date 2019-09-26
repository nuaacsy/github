import pandas as pd
import numpy as np


df_sheet=pd.read_excel("20190925//test.xlsx")
s=df_sheet.loc[1,['学号']]
for i in range(len(df_sheet)):
    df_sheet[i]
