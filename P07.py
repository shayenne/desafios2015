# Shayenne Moura
#!/usr/bin/env python

def busca_binaria(x, v):
    e = 0
    d = len(v)-1
    while e <= d:
        m = int((e+d)/2)
        if (x[0] < v[m][0] and x[1] > v[m][1]) or (x[0] >= v[m][0] and x[0] <= v[m][1]) or (x[1] >= v[m][0] and x[1] <= v[m][1]):
            return True
        if x[0] > v[m][1]:
            e = m + 1
        else:
            d = m - 1
    return False

p, q, l, r = map(int, raw_input().split())

z = []
for i in range(p):
        z.append(map(int, raw_input().split()))
	
x = []
for j in range(q):
	x.append(map(int, raw_input().split()))
	

count = 0

k = l
while k <= r:
        encaixe = False
        j = 0
        while j < len(x):
                if busca_binaria([x[j][0]+k, x[j][1]+k], z):
                        count += 1
                        break
                else:                        
                        j += 1
        k += 1

				
print count
