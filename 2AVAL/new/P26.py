"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P26 - 1195. Ouths and Crosses
"""

def calculaConfiguracao(v, nivel):
    lin = [0, 0, 0]
    col = [0, 0, 0]
    dia = [0, 0]
    for i in xrange(3):
        for j in xrange(3):
            lin[i] += v[i*3+j]
            if i == j:
                dia[0] += v[i*3+j]
            if j == 2 - i:
                dia[1] += v[i*3+j]
            col[i] += v[j*3+i]

    if verifica(dia[0], nivel):
        return verifica(dia[0], nivel)
    if verifica(dia[1], nivel):
        return verifica(dia[1], nivel)
    for i in xrange(3):
        if verifica(lin[i], nivel):
            return verifica(lin[i], nivel)
        if verifica(col[i], nivel):
            return verifica(col[i], nivel)

    return 0

def fazMovimento(v, play, nivel):

    game = calculaConfiguracao(v, nivel)
    if game or (0 not in v):
        return game

    nivel += 1
    
    total = []

    for i in xrange(len(v)):
        if v[i] == 0:
            v[i] = play
            total.append(fazMovimento(v, 0-play, nivel))
            v[i] = 0


    if play == 1:
        x = max(total)
        return x
    else:
        x = min(total)
        return x
    

def verifica(soma, nivel):
    if soma == 3:
        return 10 - nivel
    elif soma == -3:
        return nivel - 10
    else:
        return 0


if __name__ == "__main__":
    game = []
    v = []

    for i in xrange(3):
        game.append(list(raw_input())) 
    

    for i in xrange(3):
        for j in xrange(3):
            if game[i][j] == "X":
                v.append(1)
            elif game[i][j] == "O":
                v.append(-1)
            else:
                v.append(0)

    
    res = fazMovimento(v, 1, 0)


    if res > 0:
        print "Crosses win"
    elif res < 0:
        print "Ouths win"
    else:
        print "Draw"
       
