import sys

n = int(raw_input())
a = map(int, raw_input().split())

if n == 1:
    print "YES"
    exit(0)

dic = {}
for i in xrange(len(a)):
    if a[i] not in dic:
        dic[a[i]] = 0
    dic[a[i]] += 1

for v in dic:
    if dic[v] > (n+1)/2:
        print "NO"
        exit(0)

print "YES"
