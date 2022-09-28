# -*- coding: utf-8 -*-

The profit margin for popular products was increased by 10% to determine the profit increase on targetting new customers.


import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Pratham\Virtual Experience Programs\KMPG-VI\Datasets\Customers - Copy.csv')
df = np.asmatrix(df)

for i in range(len(df)):
    if df[i, 17] == 'Solex':
        df[i, 21] += 0.10 * df[i, 21]

df = pd.DataFrame(df)
df.to_csv("incr_profits.csv", index = False)
