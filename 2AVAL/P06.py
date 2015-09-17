# Shayenne Moura
#!/usr/bin/env python

k, n = map(int, raw_input().split())

cars = map(int, raw_input().split())

x = 0
for i in xrange(n):
    x += cars[i] - k

    if x < 0:
        x = 0
        
print x
