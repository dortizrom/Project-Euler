fibo = [1,2]
suma = 0

for a in range(0,100):
    if fibo[-1] % 2 == 0:
        suma += fibo[-1]
           
    fibo.append(fibo[-1]+fibo[-2])
    if fibo[-1]>4000000:
        break

print(fibo)
print(suma)
