

def calculaConfiguracao(v, play, ind):
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

    if verifica(dia[0]):
        return verifica(dia[0])
    if verifica(dia[1]):
        return verifica(dia[1])
    for i in xrange(3):
        if verifica(lin[i]):
            return verifica(lin[i])
        if verifica(col[i]):
            return verifica(col[i])


    v[ind] = 0
    chance = 0
    for i in xrange(ind+1, len(v)):
        if v[i] == 0:
            v[i] = play
            x = calculaConfiguracao(v, play, i)
            if x == -1 and play == -1:
                chance += 1
                if chance == 2:
                    return x
            elif x:
                #print "Crosses win"
                return x
            else:
                v[i] = 0
    
    
    v[ind] = play
    for i in xrange(len(v)):
        if v[i] == 0:
            v[i] = 0-play
            x = calculaConfiguracao(v, 0-play, i)
            return x
            break
            #if x == 0-play:
            #    chance+=1
            #    if chance == 2:
            #        return x
            #else:
            #    v[i] = 0
            
    
    return False
    
            
    
    
"""    
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
"""        

    

def verifica(soma):
    if soma == 3:
        #print "Crosses win"
        return 1
    elif soma == -3:
        #print "Ouths win"
        return -1
    else:
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

    for i in xrange(len(v)):
        if v[i] == 0:
            v[i] = 1
            break

    
    res = calculaConfiguracao(v, 1, i)
    if res == 1:
        print "Crosses win"
    elif res == -1:
        print "Ouths win"
    else:
        print "Draw"
       
