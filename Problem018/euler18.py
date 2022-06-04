# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:11:59 2021

@author: dorti
"""

import numpy as np
import pandas as pd
import seaborn as sns

triang = pd.read_csv("euler18.txt", sep = " ")
triang.fillna(0, inplace=True)

np_triang = np.array(triang)
print(np_triang)
print(triang.shape)

print(np.max(triang, axis=1))
print(np.max(triang, axis=0))

sns.heatmap(triang)

plt.show()
