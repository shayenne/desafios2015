#!/usr/bin/env python

p, q, l, r = map(int, raw_input().split())

z = []
for i in range(p):
	z.append(map(int, raw_input().split()))
	
x = []
for j in range(q):
	x.append(map(int, raw_input().split()))
	
	
count = 0	

for k in range(l, r+1):
	for j in range(len(x)):
		for i in range(len(z)):
			print i, j, k
			if z[i][0] <= k + x[j][0] or z[i][1]>=  k + x[j][1]:
				count += 1
				break
				
print count
