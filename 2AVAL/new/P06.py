"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P6 - 1795. Husband in a Shop
"""
#!/urs/bin/env python

m = int(raw_input())

products = {}
for i in xrange(m):
    x = raw_input().split()
    products[x[2]] = int(x[0])

    
n = int(raw_input())

cnt = 0
husbands = []
for i in xrange(n):
    x = raw_input().split()
    husbands.append([x[2], int(x[0])])

husbands.append(["Petr", 0])

x = husbands[0]
cnt = 0
while husbands[0][0] != "Petr":

    del husbands[0]
    if x[0] in products:
        if products[x[0]] >= x[1]:
            products[x[0]] -= x[1]
            if products[x[0]] == 0:
                del products[x[0]]
        else:
            husbands.insert(1, [x[0], products[x[0]]])
    
    cnt += 1
    x = husbands[0]

    
print cnt

