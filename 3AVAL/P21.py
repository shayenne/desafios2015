n = int(raw_input())

first = map(int, raw_input().split())

second = map(int, raw_input().split())


l = second.index(first[0])
qtd = 0
for i in xrange(n):
    if first[(i+1)%n] == second[(l+1)%n]:
        l+=1
    else:
        qtd += 1
        l = second.index(first[(i+1)%n])


print qtd -1
