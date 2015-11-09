global ymenor 

def compare(p, q):
    global ymenor
    x1, y1 = ymenor
    x2, y2 = p
    x3, y3 = q
    res = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
    if res < 0:
        return -1
    elif res > 0:
        return 1
    else:
        return 0
    
n = int(raw_input())

ymenor = [0, 0]

points = []

for i in xrange(n):
    x, y = map(int, raw_input().split())
    points.append([x, y])
    if y < ymenor[1]:
        ymenor = [x, y]
    elif y == ymenor[1] and x > ymenor[0]:
        ymenor = [x, y]

print ymenor
points.sort(compare)

print points

            
