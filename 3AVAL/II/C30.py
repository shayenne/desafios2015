n = int(raw_input())

cont = [0, 0]

soma = 0

last = 0
for i in xrange(n):
    op = map(int, raw_input().split())

    if op[0] == 1:
        if op[1] < len(cont)-1:
            cont[op[1]] -= op[2]
        else:
            cont[op[1]] += op[2]
        soma += op[2] * op[1]
        last = cont[-1]
        
    elif op[0] == 2:
        cont[-1] = op[1] - last
        cont.append(op[1])
        soma += cont[-1]
        
        last = cont[-1]
        
    elif op[0] == 3:
        x = cont.pop()

        last = (cont[-1] - x) * -1
        cont[-1] = last
        soma -= x
    
  
    print 1.0 * soma / (len(cont)-1)
