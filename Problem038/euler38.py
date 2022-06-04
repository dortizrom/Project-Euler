# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:55:04 2021

@author: dorti
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def IsPanDig(num):
    numstr=str(num)
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    
    for i in numstr:
        if i =='0':
            zero+=1
        if i=='1':
            one+=1
        if i=='2':
            two+=1
        if i=='3':
            three+=1
        if i=='4':
            four+=1
        if i=='5':
            five+=1
        if i=='6':
            six+=1
        if i=='7':
            seven+=1
        if i=='8':
            eight+=1
        if i=='9':
            nine+=1

    if zero ==0 and one ==1 and two==1 and three==1 and\
        four ==1 and five ==1 and six ==1 and seven==1 and\
        eight==1 and nine==1:
        return True
    else:
        return False



nlist = []
k=1
while k<1000:
    concat=""
    for i in range(1,10):
        concat = concat + str(k*i)
        if len(concat)>=9:
            break
    if IsPanDig(concat):
        nlist.append(concat)
    k+=1
    
print(max(nlist))

