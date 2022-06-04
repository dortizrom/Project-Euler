

num=1
prime_pos=1
lim=10001

while prime_pos<=lim:
    for a in range(1,num):
        if num%a==0 and a!=1:
            break
        elif a == num-1:
            print(prime_pos,num)
            prime_pos+=1
            

    num+=1
