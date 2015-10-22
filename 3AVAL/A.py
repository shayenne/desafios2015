n, m = int(raw_input().split())

array = 0 in range(n)

for i in xrange(m):
    op.append(map(int, raw_input().split()))


for i in xrange(m-1, -1, -1):
    if op[i][0] == 1:
        for j in xrange(op[i][1]-1, op[i][2]-1):
            array[j] -= op[i][3]

    if op[i][0] == 2:
        
