# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:28:26 2021

@author: dorti
"""
import time
start_time = time.time()

n=28123

def find_div(num):
    div_list=[]
    for i in range(1,num):
        if (num%i == 0):
            div_list.append(i)
    return div_list

abun = []
for i in range(1, n):
    if sum(find_div(i)) > i:
        abun.append(i)
        
sum_two_abun_dup=[]
for i in abun:
    for k in range(len(abun)):
        sum_two_abun_dup.append(i+abun[k])
    
    
# sum_two_abun = []
# for item in sum_two_abun_dup:
#     if item not in sum_two_abun:
#         sum_two_abun.append(item)

result = 0
for i in range(n+1):
    if i not in sum_two_abun_dup:
        result=result+i



#print(abun)
#print(sum_two_abun_dup[-1])

print("The result is:" + str(result))

print("--- %s seconds ---" % (time.time() - start_time))