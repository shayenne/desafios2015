#!/usr/bin/env python

import math as m

def change(move, i, j):
    p = 0
    if i-1>0 and j-1>0 and move[0][0]:
        p ^= 1 << ((i-1)*4 + (j-1))
    if i-1>0 and move[0][1]:
        p ^= 1 << ((i-1)*4 + (j))
    if i-1>0 and j+1<4 and move[0][2]:
        p ^= 1 << ((i-1)*4 + (j+1))
    if j-1>0 and move[1][0]:
        p ^= 1 << ((i)*4 + (j-1))
    if move[1][1]:
        p ^= 1 << ((i)*4 + (j))
    if j+1<4 and move[1][2]:
        p ^= 1 << ((i)*4 + (j+1))
    if i+1<4 and j-1>0 and move[2][0]:
        p ^= 1 << ((i+1)*4 + (j-1))
    if i+1<4 and move[2][1]:
        p ^= 1 << ((i+1)*4 + (j))
    if i+1<4 and j+1<4 and move[2][2]:
        p ^= 1 << ((i+1)*4 + (j+1))
            
    return p

def findSolution(conf, patt, finds, n):
    finds = range(65536)
    n = 0
    
    verify = [conf]
    finds.remove(conf)
    
    while (len(verify) > 0):
        elem = verify[0]
        print "\n---------------------------------------------\n"
        print verify
        verify.remove(elem)

        for i in xrange(16):
            new = elem ^ patt[i]
            if new in finds:
                verify.append(new)
                finds.remove(new)
                while len(lst) > 0:
                    

            if new == 65535 or new == 0:
                return "{}".format(n)
        n += 1
            
    return False



patt = []

chips = []
move = []

iniconf = 0

for i in xrange(4):
    chips.append(list(raw_input()))
    
for i in xrange(3):
    move.append(map(int, list(raw_input())))

print chips
print move


for i in xrange(4):
    for j in xrange(4):
        if chips[i][j] == "B":
            iniconf += m.pow(2, (i*4+j))
            
iniconf = int(iniconf)

print iniconf
finds = range(65536)




# Construcao dos padroes
#patt[0] = m.pow(2, 0)*pos[4] + m.pow(2, 1)*pos[5] + m.pow(2, 4)*pos[7] + m.pow(2, 5)*pos[8]
#patt[1] = m.pow(2, 0)*pos[3] + m.pow(2, 1)*pos[4] + m.pow(2, 2)*pos[5] + m.pow(2, 4)*pos[6] + m.pow(2, 5)*pos[7] + m.pow(2, 6)*pos[8]
#patt[2] = m.pow(2, 1)*pos[3] + m.pow(2, 2)*pos[4] + m.pow(2, 3)*pos[5] + m.pow(2, 5)*pos[6] + m.pow(2, 6)*pos[7] + m.pow(2, 7)*pos[8]
#patt[3] = m.pow(2, 2)*pos[3] + m.pow(2, 3)*pos[4] + m.pow(2, 6)*pos[6] + m.pow(2, 7)*pos[7]
#patt[4] = m.pow(2, 0)*pos[1] + m.pow(2, 1)*pos[2] + m.pow(2, 4)*pos[4] + m.pow(2, 5)*pos[5] + m.pow(2, 8)*pos[7] + m.pow(2, 9)*pos[8]
#patt[5] = m.pow(2, 0)*pos[0] + m.pow(2, 1)*pos[1] + m.pow(2, 2)*pos[2] + m.pow(2, 4)*pos[3] + m.pow(2, 5)*pos[4] + m.pow(2, 6)*pos[5] + m.pow(2, 8)*pos[6] + m.pow(2, 9)*pos[7] + m.pow(2, 10)*pos[8]
#patt[6] = m.pow(2, 1)*pos[0] + m.pow(2, 2)*pos[1] + m.pow(2, 3)*pos[2] + m.pow(2, 5)*pos[3] + m.pow(2, 6)*pos[4] + m.pow(2, 7)*pos[5] + m.pow(2, 9)*pos[6] + m.pow(2, 10)*pos[7] + m.pow(2, 11)*pos[8]


#patt[9] = m.pow(2, 4)*pos[0] + m.pow(2, 5)*pos[1] + m.pow(2, 6)*pos[2] + m.pow(2, 8)*pos[3] + m.pow(2, 9)*pos[4] + m.pow(2, 10)*pos[5] + m.pow(2, 12)*pos[6] + m.pow(2, 13)*pos[7] + m.pow(2, 14)*pos[8]
#patt[10] = m.pow(2, 5)*pos[0] + m.pow(2, 6)*pos[1] + m.pow(2, 7)*pos[2] + m.pow(2, 9)*pos[3] + m.pow(2, 10)*pos[4] + m.pow(2, 11)*pos[5] + m.pow(2, 13)*pos[6] + m.pow(2, 14)*pos[7] + m.pow(2, 15)*pos[8]

###

empty = []
for i in xrange(4):
    for j in xrange(4):
        patt.append( change(move, i, j))

            

print patt

result = findSolution(iniconf, patt, finds, 0)
if result:
    print result
else:
    print "Impossible"
