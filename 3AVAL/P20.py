w, h  = map(int, raw_input().split())

t = 0
i = 2

while i <= w and i <= h:
        t += (w - i + 1)*(h - i + 1)
        i += 2
        

print t