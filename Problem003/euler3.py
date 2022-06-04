

import time
start_time = time.time()

num=76576500

pfactor=[]
n=1
mult=1
while n<num:
    if num%n == 0:
        pfactor.append(n)
        mult*=n
        if mult == num:
            break   
            
    n+=1

print(pfactor)

print("--- %s seconds ---" % (time.time() - start_time))

