

def calculaConfiguracao(v, play):
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
        col[i] += v[i*3]

    if verifica(dia[0]) or verifica(dia[1]):
        return True
    for i in xrange(3):
        if verifica(lin[i]) or verifica(col[i]):
            return True

    new = v
    for i in xrange(len(new)):
        if new[i] == 0:
            print new
            new[i] = play
            print new
            if not calculaConfiguracao(new, 0-play):
                print "Entrei no not"
                new[i] = 0
                print new
            else:
                return True
        
    return False 
    

def verifica(soma):
    if soma == 3:
        print "Crosses win"
        return True
    elif soma == -3:
        print "Ouths win"
        return True
    else:
        print "Calma"
        return False


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

    if not calculaConfiguracao(v, 1):
        print "Draw"

    
