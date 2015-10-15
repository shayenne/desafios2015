

                

game = []
for i in xrange(3):
    game.append(list(raw_input()))


linha  = 0 for i in range(3)
coluna = 0 for i in range(3)
diag1  = 0
diag2  = 0
for i in xrange(3):
    for j in xrange(3):
    	
    	if game[i][j] == "X":
	    linha[i]  += 1
	    coluna[j] += 1
	    if i == j:
	        diag1 += 1
            if j == 2-i:
                diag2 += 1
	elif game[i][j] == "O":
	    linha[i]  -= 1
	    coluna[i] -= 1
	    if i == j:
                diag1 -= 1
            if j == 2-i:
                diag2 -= 1
	

for i in xrange(3):
    if linha[i] or coluna[i] == 2:
        print "Cruzes win"
    elif linha[i] or coluna[i] == -2:
        print "Ouths win"
    else:
        print "Draw"
                
