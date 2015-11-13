"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P19 - 189A. Cut Ribbon
"""

nums = map(int, raw_input().split())
n = nums[0]
del nums[0]
nums.sort()

a, b, c = nums

mem = 0

if n % a == 0:
    print n/a
else:
    conj = set([a, b, c])
    if len(conj) == 2:
        a, b = conj
        for i in xrange(1 + n/b):
            if (n - i * b) % a == 0:
                print i + (n - i * b) / a
                break
    else:
        for i in xrange(1 + n/c):
            for j in xrange(1 + n/b):
                if (n - i*c - j*b) % a == 0:
                    val = i+j + (n - i*c - j*b) / a
                    if val > mem:
                        mem = val

                
        print mem


