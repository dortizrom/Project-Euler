import time
start_time = time.time()

def prime(x):
    if x == [0,1]:
        return False
    elif x==2:
        return True
    elif x>2:
        for a in range(2,int(x**0.5+1)):
            if x%a==0:
                return False
    return True

#test
#print(prime(9))

lprime=[2]
lim=2*10**6

for num in range(3,lim):
    if prime(num)==True:
        lprime.append(num)

print(sum(lprime))
print("--- %s seconds ---" % (time.time() - start_time))
