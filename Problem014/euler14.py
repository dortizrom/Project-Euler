# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:25:39 2021

@author: dorti
"""


import time 
start_time = time.time()


long = 0
for i in range(1000000):
    N = i
    list = [N]
    
    while N>1:
        if N%2 == 0:
            N = N/2
            list.append(N)
        elif N%2 != 0:
            N = 3*N+1
            list.append(N)
        # elif N==1 or N<1:
        #     break
    if len(list) > long:
        long = len(list)
        starting_number = i

print(starting_number)
print("--- %s seconds ---" % (time.time() - start_time))
    
