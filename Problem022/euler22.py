# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:13:13 2021

@author: dorti
"""

import numpy as np
import pandas as pd

names = pd.read_csv('names.txt')

names = names.T.reset_index()

names.columns = ["NAMES"]
names.sort_values("NAMES", inplace=True)
names.reset_index(drop = True, inplace=True)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = list(np.arange(1,len(letters)+1))
zip_iterator =zip(letters, numbers)
dictionary = dict(zip_iterator)

sum = 0
i = 0
for n in names.NAMES:
    score = 0
    i = i+1
    for k in n:
        score = score + dictionary[k]
        
    sum = sum + score*i
    
print(sum)    
        

