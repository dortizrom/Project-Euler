# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:48:25 2021

@author: dorti
"""

def factorial(n):
    factorial = n
    for n in range(1,n):
        factorial = factorial * n
    return factorial

strfact = str(factorial(100))

sumfact = 0
for i in strfact:
    sumfact += int(i)
    
print(sumfact)