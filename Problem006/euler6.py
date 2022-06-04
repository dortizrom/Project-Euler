sum_of_sqr=[]
sqr_of_sum=[]


for a in range(1,101):
    sum_of_sqr.append(a**2)
    sqr_of_sum.append(a)

print(sum_of_sqr)
print(sqr_of_sum)

sum_of_sqr=sum(sum_of_sqr)
sqr_of_sum=sum(sqr_of_sum)**2

dif=sqr_of_sum-sum_of_sqr
print(dif)
