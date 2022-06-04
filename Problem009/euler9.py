

for a in range(1,501):
    for b in range(1,501):
        if ((a**2+b**2)**0.5==(1000-a-b)):
            print("a="+str(a)+","+"b="+str(b))
            break
    if ((a**2+b**2)**0.5==(1000-a-b)):
        break
    
    
c=1000-a-b

print("c="+str(c))
print(a*b*c)
