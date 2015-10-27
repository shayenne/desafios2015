import math
import sys

all_input = iter(sys.stdin.read().strip().replace('\n', ' ').split(' '))

n = int(all_input.next())

city = []

for i in xrange(n):

    city.append([int(all_input.next()), int(all_input.next())])

R = int(all_input.next())
r = int(all_input.next())

if   R < r:
    print 0
elif R == r:
    print 1
else:
    total = 1
    for i in xrange(n):
        num = 0
        conj = []
        for j in xrange(i, n):
            dist = math.sqrt((city[i][0]-city[j][0])*(city[i][0]-city[j][0]) +
                             (city[i][1]-city[j][1])*(city[i][1]-city[j][1]))
            if dist + 2*r <= 2*R:
                
                conj.append(city[j])
                num += 1
                    
                for c in conj:
                    dist = math.sqrt((city[j][0]-c[0])*(city[j][0]-c[0]) +
                                     (city[j][1]-c[1])*(city[j][1]-c[1]))
                    if dist + 2*r > 2*R:
                        conj.remove(city[j])
                        num -= 1
                        
                            

        if total < num:
            total = num

    print total
