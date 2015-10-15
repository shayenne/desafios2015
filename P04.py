#!/usr/bin/env python

def binary_search(x, v):
	e = 0
	d = len(v)-1
	while e <= d:
		m = int((e+d)/2)
		if x == v[m]:
			return m
		
		if x > v[m]:
			e = m + 1 
		else:
			d = m - 1
	return -1


n = int(raw_input())

m = map(int, raw_input().split())

p = []
g = []

pcnt = 0
gcnt = 0
for i in range(n):
	if m[i] == 1:
		pcnt += 1
	else:
		gcnt += 1

	p.append(pcnt) 
	g.append(gcnt)

tmax = max(p[n-1], g[n-1])

print p
print g
print tmax
