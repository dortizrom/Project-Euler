# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:06:55 2022

@author: dorti
"""


sum =0
for n in range(1, 1001):
    sum += n**n
    
resp = str(sum)
print(resp)
print(resp[-10:])
