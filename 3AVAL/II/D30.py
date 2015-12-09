g = {1:(-1, -1)}

def calculaCaminhoMore(x, a, n):
    global g

    if x <= 0 or x > n:
        return True

    if x in g:
        return False
    
    v = calculaCaminho(x+a[x], a, n)
    
    if v:
        more = a[x] + v
    else:
        g[x] = -1
        return -1

    g[x] = more
    
    return 0




n = int(raw_input())
a = [0, 1]
a += map(int, raw_input().split())
"""
print a

for i in xrange(2, n+1):
    if i not in g:
        calculaCaminho(i, a, n)

    
print g
"""

cls = []

for i in xrange(1, n):
    cycle = False
    states = [1, i+1]
    x = i+1
    y = i

    a[1] = x

    for j in xrange(1, n):
        v = a[x]
        if j % 2 != 0:
            x -= v
        else:
            x += v

        y += v
        
        if x <= 0 or x > n:
            break

        if x in states or x in cls:
            print -1
            cycle = True
            cls += states
            break
        else:
            states.append(x)

    if not cycle:
        print y
