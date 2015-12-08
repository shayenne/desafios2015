
"""
# d = 1 soma, d = 0 subtrai
def calculaCaminho(a, dp, i, d, n):
    global visto

    visto.append(i)
    if d == 1:
        v = i + a[i]
    else:
        v = i - a[i]

    if v in visto:
        dp[i][d] = -1
        return -1

    if v <= 0 or v > n:
        dp[i][d] = a[i]
        return a[i]

    else:
        if d == 0:
            x = calculaCaminho(a, dp, v, 1, n)
        else:
            x = calculaCaminho(a, dp, v, 0, n)

        if x == -1:
            dp[i][d] = -1
            return -1
        else:
            dp[i][d] = a[i] + x
    
    return 0
    
"""
n = int(raw_input())

a = [0, 1] + map(int, raw_input().split())

dp = [[-1, -1] for i in xrange(n+2)]



for i in xrange(2, n+1):
    visto = [0 for j in xrange(n+1)]
    x = []
    ref = []
    d = 0
    visto[i] = 1
    visto[1] = 1
    end = False

    while not end:
        if d == 1:
            v = i + a[i]
        else:
            v = i - a[i]


        if v > 0 and v <= n and visto[v] == 1:
            dp[i][d] = -1
            x.append(-1)
            end = True
            break

        if v <= 0 or v > n:
            #dp[i][d] = a[i]
            ref.append([i, d])
            x.append(a[i])
            end = True
            break
        else:      
            ref.append([i, d])
            x.append(a[i])
            if d == 0:
                i = v
                d = 1
                #x = calculaCaminho(a, dp, v, 1, n)
            else:
                i = v
                d = 0
                #x = calculaCaminho(a, dp, v, 0, n)

        visto[v] = 1


    if x[-1] == -1:
        for r in ref:
            dp[r[0]][r[1]] = -1
    else:
        soma = 0
        while len(ref) > 0:
            soma += x.pop()
            q = ref.pop()
            dp[q[0]][q[1]] = soma


for i in xrange(1, n):
    if dp[i+1][0] != -1:
        print i + dp[i+1][0]
    else:
        print -1
