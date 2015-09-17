#!/urs/bin/env python

m = int(raw_input())

products = {}
for i in xrange(m):
    x = raw_input().split()
    products[x[2]] = int(x[0])

    
n = int(raw_input())

cnt = 0
husbands = []
for i in xrange(m):
    x = raw_input().split()
    
    if x[2] in products and products[x[2]] >= x[0]:
        products[x[2]] -= x[0]
        if products[x[2]] == 0:
            del products[x[2]]
    else:
        husbands.append([x[2], int(x[0])])
    

print products
