w, h  = map(int, raw_input().split())

t = 0
i = 2
j = 2

while i <= w:
        j = 2
        while  j <= h:
                t += (w - i + 1)*(h - j + 1)
                j += 2
        i += 2



# Segunda solucao
#t = (h/2)*(h-(h/2))*(w/2)*(w-(w/2))

print t
