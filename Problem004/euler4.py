import numpy as np
n_min = 10000
n_max = 998001

n_min3 = 100
n_max3 = 999

pali = []

for a in range(n_min, n_max):
	s = str(a)
	s_inv = int((s[::-1]))
	if s_inv == a:
		pali.append(a)
		
for k in pali:
	for j in range(n_min3, n_max3):
		if k%j == 0:
			if (k/j > 100) and (k/j<1000):
				print(str(j) + " * "+str(k/j)+ "=" +str(k))
