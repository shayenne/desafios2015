def binary_search(a, e, d, x, y):
    if e > d:
        return False

    m = (e + d)/2
    if a[m][0] == x and a[m][1] == y:
        return True
    elif a[m][0] <= x and a[m][1] < y:
        return binary_search(a, m+1, d, x, y)
    elif (a[m][0] <= x and a[m][1] > y) or a[m][0] > x:
        return binary_search(a, e, m-1, x, y)

    return False

n = int(raw_input())

pts = []

for i in xrange(n):
    x, y = map(int, raw_input().split())
    pts.append((x, y))
pts.sort()
#pts.sort(key=lambda tup:tup[1])
#pts.sort(key=lambda tup:tup[0])


grps = 0
for i in xrange(n-2):
    for j in xrange(i+2, n):
        x = (pts[i][0]+pts[j][0])/2.0
        y = (pts[i][1]+pts[j][1])/2.0
        
        if binary_search(pts, i, j, x, y):
            grps += 1

print grps    
