import sys

n, m = map(int, raw_input().split())

op = []
array = [int(1E9) for i in range(n)]
#med = [0 for i in range(n)]
diff = [0 for i in range(n)]

#print array
for i in xrange(m):
    op.append(map(int, raw_input().split()))

    if op[i][0] == 1:
        for j in xrange(op[i][1]-1, op[i][2]):
            #if array[j] != "*":
            #array[j] += op[i][3]
            diff[j]  += op[i][3]

    elif op[i][0] == 2:
        rigth = False
        for j in xrange(op[i][1]-1, op[i][2]):
            if array[j] >= op[i][3] - diff[j]:
                array[j] = op[i][3] - diff[j]
                rigth = True
        if not rigth:
            print "NO"
            exit(0)

"""            
for i in range(n):
    if array[i] != "*":
        array[i] -= diff[i]
    else:
        array[i] = 0
"""

        
test = array[:]
#print test


for i in xrange(m):
    if op[i][0] == 1:
        for j in xrange(op[i][1]-1, op[i][2]):
            test[j] += op[i][3]

    
    elif op[i][0] == 2:
        right = False
        for j in xrange(op[i][1]-1, op[i][2]):
            if test[j] > op[i][3]:
                print "NO"
                exit(0)
            
            if test[j] == op[i][3]:
                right = True            
    
        if not right:
            print "NO"
            exit(0)
            
            
print "YES"
print " ".join(str(x) for x in array)
