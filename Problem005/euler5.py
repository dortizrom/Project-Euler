import numpy as np

dv_num=0
check=0
num=1
rango=20
while True:
    for a in range(rango,0,-1):
        if num%a == 0:
            check+=1
        else:
            break
    if check == rango:
        dv_num = num
        break

    num+=1
    check=0

print(dv_num)
