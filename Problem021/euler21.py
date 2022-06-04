# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:24:23 2021

@author: dorti
"""

import numpy as np

def div(num):
    div_array=np.empty(0)
    for i in range(1,int(num/2+1)):
        if (num%i == 0):
            div_array = np.append(div_array, i)
    return np.sum(div_array)

amic = np.empty(0)

for i in range(1, 10001):
    a = i
    b = div(a)
    if div(a) == b and div(b) == a and a != b:
        amic = np.append(amic, [a, b])    

amic = np.unique(amic)
print(amic)
print(np.sum(amic))