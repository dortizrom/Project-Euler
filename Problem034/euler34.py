# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:32:42 2022

@author: dorti
"""

import numpy as np

resp = 0
for n in range(3, 362880):
    
    x = str(n)
    sum=0
    for d in x:
        sum += np.math.factorial(int(d))
    
    if(sum == n):
        resp += n
        print(n)
        

print(resp)

