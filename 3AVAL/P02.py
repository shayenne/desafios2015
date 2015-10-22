import math

x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())


xbar = (x1 + x2 + x3)/3.0
ybar = (y1 + y2 + y3)/3.0




#AB = (y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1
#AC = (y1 - y3) * x + (x3 - x1) * y + x1 * y3 - x3 * y1
#BC = (y2 - y3) * x + (x3 - x2) * y + x2 * y3 - x3 * y2
#reta = (yn - ybar) * x + (xbar - xn) * y + xn * ybar - xbar * yn

AB = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
CB = math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
CA = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))

theta = math.acos((AB*AB - CA*CA - CB*CB)/(-2.0*CA*CB))

P = AB + CA + CB

soma = P/2.0

Area = math.sqrt(soma*(soma-AB)*(soma-CA)*(soma-CB))

print theta
print math.sin(theta)

prod = Area/math.sin(theta)

r1 = (soma + math.sqrt(soma*soma - 4 * prod))/2.0

r2 = (soma - math.sqrt(soma*soma - 4 * prod))/2.0


s1 = soma - r1

s2 = soma - r2

if s1 <= CA:
    p, q = x3 + s1* (x3 - x1), y3 + s1 * (y3 - y1)
    k, l = x3 + r1* (x3 - x2), y3 + r1 * (y3 - y2)
else:
    p, q = x3 + s2* (x3 - x1), y3 + s2 * (y3 - y1)
    k, l = x3 + r2* (x3 - x2), y3 + r2 * (y3 - y2)

print AB, CB, CA, theta, math.pi/2
print s1, r1, 
print p, q
print k, l
