#n = int(raw_input())

import math

def eh_primo(k):
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

count = 0
for i in range(1000, 10000):
    if eh_primo(i):
        count +=1



print count
