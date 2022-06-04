# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 01:53:15 2021

@author: dorti
"""
import numpy as np
import time
start_time = time.time()

def find_n_div(num):
    div_list=[]
    for i in range(1,int(num/2+1)):
        if (num%i == 0):
            div_list.append(i)
    return len(div_list)


def triang(n):
    triangular = np.sum(range(n+1))
    return triangular


n=1
while (find_n_div(triang(n))<=500):
    print(find_n_div(triang(n)), triang(n))
    n+=1

print("--- %s seconds ---" % (time.time() - start_time))

