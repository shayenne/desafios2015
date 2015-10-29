import math

def encontraReta(x1, y1, x2, y2, x3, y3, A, B, C, Area, soma):
    theta = math.acos((C*C - B*B - A*A)/(-2.0*A*B))
    #prod = Area/math.sin(theta)
    prod  = A*B/2.0
    delta = soma*soma - 4*prod
    #print soma*soma, math.sin(theta), prod
    print delta
    #if delta < 0:
    #    delta *= -1
    
    r1 = (soma + math.sqrt(delta))/2.0
    r2 = (soma - math.sqrt(delta))/2.0

    s1 = soma - r1
    s2 = soma - r2

    #print "{0:.12f}".format(soma), "{0:.12f}".format(s1+r1), "{0:.12f}".format(s2+r2)

    if r1 <= B and s1 <= A:    
        p, q = x3 + (r1/B)* (x1 - x3), y3 + (r1/B) * (y1 - y3)
        k, l = x3 + (s1/A)* (x2 - x3), y3 + (s1/A) * (y2 - y3)
    elif r2 <= B and s2 <= A:
        p, q = x3 + (r2/B)* (x1 - x3), y3 + (r2/B) * (y1 - y3)
        k, l = x3 + (s2/A)* (x2 - x3), y3 + (s2/A) * (y2 - y3)
    else:
        return None

    return [p, q, k, l]


x1, y1, x2, y2, x3, y3 = map(float, raw_input().split())

#AB = (y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1
#AC = (y1 - y3) * x + (x3 - x1) * y + x1 * y3 - x3 * y1
#BC = (y2 - y3) * x + (x3 - x2) * y + x2 * y3 - x3 * y2
#reta = (yn - ybar) * x + (xbar - xn) * y + xn * ybar - xbar * yn

C = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
A = math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
B = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))

P = A + B + C

soma = P/2.0

Area = ((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y2))/2.0

#Area = math.sqrt(soma*(soma-A)*(soma-B)*(soma-C))



resp = encontraReta(x1, y1, x2, y2, x3, y3, A, B, C, Area, soma)
if resp == None:
    resp =  encontraReta(x2, y2, x3, y3, x1, y1, B, C, A, Area, soma)
if resp == None:
    resp =  encontraReta(x1, y1, x3, y3, x2, y2, A, C, B, Area, soma)
if resp == None:
    print "NO"
    exit(0)

    
print "YES"            
print "{0:.15f}".format(resp[0]), "{0:.15f}".format(resp[1])
print "{0:.15f}".format(resp[2]), "{0:.15f}".format(resp[3])


