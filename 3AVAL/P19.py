n, a, b, c = map(int, raw_input().split())

def mdc(a, b):
     # aqui comeca o algoritmo de Euclides
    anterior = a
    atual    = b
    resto    = anterior % atual
    
    while resto != 0:
        anterior = atual
        atual    = resto
        resto    = anterior % atual
        
    return [atual, resto, anterior]

def encontraMaximo(x0, b, y0, a):
    t = 0;
    velho = novo = x0+y0
    
    while novo <= velho:
        t += 1
        velho, novo = novo, x0+(b*t) + y0-(a*t)

    return velho

m = min(a, b, c)

if (n % m == 0):
    print n/m

else:
    maximo = 0
    for i in xrange(3):
        if a != b:
           d = mdc(a, b)

           if n % d[0] == 0:
               x0 = d[1]
               y0 = d[2]
               val = encontraMaximo(x0, b/d[0], y0, a/d[0])
               
               if val > maximo:
                   maximo = val

        a, b, c = b, c, a


    if a != b and b != c and c != a:
        print "Ainda nao achei a resposta"

    print maximo
