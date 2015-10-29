import sys

n, m = map(int, raw_input().split())

op = []
a = [0 for i in range(n)]
med = [0 for i in range(n)]
d = [0 for i in range(n)]

print a, med, d

for i in xrange(m):
    op.append(map(int, raw_input().split()))


for i in xrange(m):
    if op[i][0] == 1:
        for j in xrange(op[i][1]-1, op[i][2]):
            d[j] += op[i][3]
            #a[j] = med[j] - d[j]

    if op[i][0] == 2:
        for j in xrange(op[i][1]-1, op[i][2]):
            med[j] = op[i][3]
            a[j] = med[j] - d[j]
            for k in xrange(op[i][1]-1, op[i][2]):
                if a[k] > med[j]:
                    print "NO"
                    exit
            
            
#for i in xrange(n):
#    a[i] = med[i] - d[i]

print a
