n = int(raw_input())

first = map(int, raw_input().split())

second = map(int, raw_input().split())


l = first.index(1)
qtd = 0
for i in xrange(n):
    if first[(i+l+1)%n] >= first[(i+l)%n]:
        qtd += 1
    else:
        break


print n - qtd
