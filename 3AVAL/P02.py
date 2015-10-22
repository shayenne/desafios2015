import math

def encontraReta(x1, y1, x2, y2, x3, y3, A, B, C, Area, soma):
    theta = math.acos((C*C - B*B - A*A)/(-2.0*A*B))
    prod = Area/math.sin(theta)
    
    r1 = (soma + math.sqrt(soma*soma - 4 * prod))/2.0
    r2 = (soma - math.sqrt(soma*soma - 4 * prod))/2.0

    s1 = soma - r1
    s2 = soma - r2


    print r1, s1
    print A, B
    if r1 <= B and s1 <= A:
        print "Entrei no primeiro"
        print r1/B, s1/A, y3 + (r1/B)* (y3 - y1)
        p, q = x3 + (r1/B)* (x3 - x1), y3 + (r1/B) * (y3 - y1)
        k, l = x3 + (s1/A)* (x3 - x2), y3 + (s1/A) * (y3 - y2)
        print p, q, k, l
    elif r2 <= A and s2 <= B:
        print "Entrei no segundo"
        p, q = x3 + r2/A* (x3 - x1), y3 + r2/A * (y3 - y1)
        k, l = x3 + s2/B* (x3 - x2), y3 + s2/B * (y3 - y2)
    else:
        print "Retornei None"
        return None

    return [p, q, k, l]


x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())

#AB = (y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1
#AC = (y1 - y3) * x + (x3 - x1) * y + x1 * y3 - x3 * y1
#BC = (y2 - y3) * x + (x3 - x2) * y + x2 * y3 - x3 * y2
#reta = (yn - ybar) * x + (xbar - xn) * y + xn * ybar - xbar * yn

C = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
A = math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
B = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))

P = A + B + C

soma = P/2.0

Area = math.sqrt(soma*(soma-A)*(soma-B)*(soma-C))

resp = encontraReta(x1, y1, x2, y2, x3, y3, A, B, C, Area, soma)
if resp == None:
    resp =  encontraReta(x2, y2, x3, y3, x1, y1, B, C, A, Area, soma)
    if resp == None:
        resp =  encontraReta(x1, y1, x3, y3, x2, y2, A, C, B, Area, soma)
        if resp == None:
            print "No"
            exit(0)
            
print "{0:.10f}".format(resp[0]), "{0:.10f}".format(resp[1])
print "{0:.10f}".format(resp[2]), "{0:.10f}".format(resp[3])
print A, B, C

