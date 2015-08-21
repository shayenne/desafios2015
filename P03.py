# Shayenne Moura
#!/usr/bin/env python

import numpy as np

inds = raw_input()
inds = inds.split()
n = int(inds[0])
m = int(inds[1])

words = []

for i in range(n):
    line = list(raw_input())
    words.append(line)


def remove_coluna(n, j, a=[], *args):
    for i in range(n):
        del a[i][j]
    

def matriz_boa(a=[], *args):
    if len(a) == 0 or len(a) == 1:
        return 0

    i = 0
    j = 0
    while i < len(a)-1:
        while j < len(a[i]):
            if a[i][j] > a[i+1][j]:
                remove_coluna(len(a), j, a)
                return matriz_boa(a) + 1
            elif a[i][j] < a[i+1][j]:
                break
            else: 
                j+=1

        i+=1
        j = 0

    return 0


print matriz_boa(words)



