n = int(raw_input())

a = [0, 1]

a += map(int, raw_input().split())

gmore = {1:"FIM"}

gless = {1:"FIM"}

for i in xrange(2, n+1):
    if i + a[i] <= n: 
        gmore[i] = i + a[i]
    else:
        gmore[i] = "FIM"
        
    if i - a[i] > 0:
        gless[i] = i - a[i]
    else:
        gless[i] = "FIM"




for i in xrange(1, n):
    cycle = False
    states = [1, i+1]
    y = i
    x = i+1
    for j in xrange(1, n):
        y += a[x]
        if j % 2 != 0:
            if gless[x] != "FIM":
                x = gless[x]
            else:
                break

        else:
            if gmore[x] != "FIM":
                x = gmore[x]
            else:
                break


        if x in states:
            print -1
            cycle = True
            break
        else:
            states.append(x)
        
    if not cycle:
        print y
