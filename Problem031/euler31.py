# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:09:22 2022

@author: dorti
"""



combinacion = 0
valor=0

for a in range(0,201):
    valor = 1*a
    if(valor>200):
        break
    for b in range(0,101):
        valor = 1*a+2*b
        if(valor>200):
            break
        for c in range(0,41):
            valor = 1*a+2*b+5*c
            if(valor>200):
                break
            for d in range(0,21):
                valor = 1*a+2*b+5*c+10*d
                if(valor>200):
                    break
                for e in range(0,11):
                    valor = 1*a+2*b+5*c+10*d+20*e
                    if(valor>200):
                        break
                    for f in range(0,5):
                        valor = 1*a+2*b+5*c+10*d+20*e+50*f
                        if(valor>200):
                            break
                        for g in range(0,3):
                            valor = 1*a+2*b+5*c+10*d+20*e+50*f+100*g
                            if(valor>200):
                                break
                            for h in range(0,2):
                                valor = 1*a+2*b+5*c+10*d+20*e+50*f+100*g+200*h
                                if(valor>200):
                                    break
                                if(valor==200):
                                    combinacion += 1
    
print(combinacion)