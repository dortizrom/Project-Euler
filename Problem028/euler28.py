# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:30:57 2022

@author: dorti
"""

import numpy as np

sum=1
for n in range(3, 1002, 2):
    a = n**2
    b = n**2-3*n+3
    c = n**2-2*n+2
    d = n**2-n+1
    
    sum += a+b+c+d
    
print(sum)