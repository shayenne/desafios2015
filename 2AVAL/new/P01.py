"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P1 - 1122. Game
"""
#!/usr/bin/env python

import math as m

def change(move, i, j):

    p = 0
    
    if i - 1 >= 0 and j - 1 >= 0 and move[0][0]:
        p ^= 1 << ((i-1)*4 + (j-1))
    if i - 1 >= 0 and move[0][1]:
        p ^= 1 << ((i-1)*4 + (j))
    if i - 1 >= 0 and j + 1 < 4 and move[0][2]:
        p ^= 1 << ((i-1)*4 + (j+1))
    if j - 1 >= 0 and move[1][0]:
        p ^= 1 << ((i)*4 + (j-1))
    if move[1][1]:
        p ^= 1 << ((i)*4 + (j))
    if j + 1 < 4 and move[1][2]:
        p ^= 1 << ((i)*4 + (j+1))
    if i + 1 < 4 and j - 1 >= 0 and move[2][0]:
        p ^= 1 << ((i+1)*4 + (j-1))
    if i + 1 < 4 and move[2][1]:
        p ^= 1 << ((i+1)*4 + (j))
    if i + 1 < 4 and j + 1 < 4 and move[2][2]:
        p ^= 1 << ((i+1)*4 + (j+1))
            
    return p

def findSolution(conf, patt, finds, n):
    finds = [False]*65536
    n = 0
    
    if conf == 65535 or conf == 0:
        return "{}".format(n)
    
    verify = [conf]
    finds[conf] = True
    n+=1
    while (len(verify) > 0):
        lst = []
        
        while(len(verify) > 0):
            elem = verify[0]

            verify.remove(elem)

            for i in xrange(16):
                new = elem ^ patt[i]
            
                if new == 65535 or new == 0:
                    return "{}".format(n)
            
                if not finds[new]:
                    lst.append(new)
                    finds[new] = True

        
        verify = lst        
        n += 1
            
    return False







patt = []
chips = []
move = []

iniconf = 0
for i in xrange(8):
    chips
    
for i in xrange(4):
    chips.append(list(raw_input()))
    
for i in xrange(3):
    move.append(map(int, list(raw_input())))


for i in xrange(4):
    for j in xrange(4):
        if chips[i][j] == "B":
            iniconf += m.pow(2, (i*4+j))
            
iniconf = int(iniconf)

finds = range(65536)




empty = []
for i in xrange(4):
    for j in xrange(4):
        patt.append( change(move, i, j))

        
result = findSolution(iniconf, patt, finds, 0)
if result:
    print result
else:
    print "Impossible"
