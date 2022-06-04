

fibo =[1,1]

while len(str(fibo[-1])) < 1000:
    fibo.append(fibo[-1]+fibo[-2])


print(fibo[-1])
print("largo del numero: " +str(len(str(fibo[-1]))))
print("index: " + str(fibo.index(fibo[-1])+1))
