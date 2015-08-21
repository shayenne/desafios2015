# Shayenne Moura
#!/usr/bin/env python

from sys import exit

n = int(raw_input())

p = raw_input()
q = raw_input()

p = p.split()
q = q.split()

p = map(int, p)
q = map(int, q)
del p[0]
del q[0]

x = []
x = p+q

x.sort()
w = list(set(x))


i = 0
j = 0

if len(w) < n:
    print "Oh, my keyboard!"
else:
    print "I become the guy."

