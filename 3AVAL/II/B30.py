n = int(raw_input())

cows = list(raw_input())

a = i = 0

for j in xrange(n):
    if cows[j] == "A":
        a += 1

    elif cows[j] == "I":
        i += 1

if i == 1:
    print 1
elif i == 0:
    print a
else:
    print 0
