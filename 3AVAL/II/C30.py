n = int(raw_input())

cont = [0]
md = 0
soma = 0
media = 0
last = 0
for i in xrange(n):
    op = map(int, raw_input().split())

    if op[0] == 1:
        cont[op[1]-1] += op[2]
        soma += op[2]
        
    elif op[0] == 2:
        cont.append(op[1] - last)
        soma += cont[-1]
        
        last.append(op[1])
        
    elif op[0] == 3:
        x = cont.pop()
        soma -= x
        
        md += x
        media -= last.pop()


    print op, last, cont,media
    md -= (3*last[len(last)-1])
    print md
        
    print 1.0 * media / len(cont)
