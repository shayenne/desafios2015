

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
            col[i] += v[j*3+i]
            
    if verifica(dia[0]):
        return verifica(dia[0])
    if verifica(dia[1]):
        return verifica(dia[1])
    for i in xrange(3):
        print lin[i], col[i]
        if verifica(lin[i]):
            return verifica(lin[i])
        if verifica(col[i]):
            return verifica(col[i])
    

    return False

def fazMovimento(v, play, ind):
    if calculaConfiguracao(v, play, ind):
        return play
    
    
    testa = [v[:]]
    
    v[ind] = 0
    #chance = 0
    for i in xrange(ind+1, len(v)):
        if v[i] == 0:
            v[i] = play
            x = calculaConfiguracao(v, play, i)
            #if x == -1 and play == -1:
            #    chance += 1
            #    if chance == 2:
            #        return x
            if x:
                #print "Crosses win"
                return x
            else:
                testa.append(v[:])
                v[i] = 0
                
    print testa
    ver = []
    for w in testa:
        chance = 0
        print w
        for i in xrange(len(w)):
            if w[i] == 0:
                w[i] = 0-play
                x = calculaConfiguracao(w, 0-play, i)
                print x
                if x == -1:
                    chance += 1
                    if chance == 2:
                        return x
                    
                    ver.append(w[:])
                    w[i] = 0
                elif x == 0:
                    w[i] = play
                    q = w.index(0)
                    w[q] = 0-play
                    if not calculaConfiguracao(w, 0-play, i):
                        ver.append(w[:])
                    else:
                        w[i] = 0-play
                        w[q] = 0
                        
                        ver.append(w[:])
                    w[i] = 0
            
            
            #if x == 0-play:
            #    chance+=1
            #    if chance == 2:
            #        return x
            #else:
            #    v[i] = 0
            
    for u in ver:
        for i in xrange(len(u)):
            if u[i] == 0:
                u[i] = play
                x = calculaConfiguracao(u, play, i)
                print x
                if x == 1:
                    return x
                break
    
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

    print v
    for i in xrange(len(v)):
        if v[i] == 0:
            v[i] = 1
            break
    print v
    
    res = fazMovimento(v, 1, i)
    if res == 1:
        print "Crosses win"
    elif res == -1:
        print "Ouths win"
    else:
        print "Draw"
       
