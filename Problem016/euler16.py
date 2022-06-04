# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 01:40:14 2021

@author: dorti
"""


num = str(2**1000)

sum = 0
for i in num:
    n = int(i)
    sum += n
    
print(sum)