L = int(input())
if 1<=L<=1000000:
    c = 0
    while L > 0:
        if L >= 5:
            L -= 5
            c += 1
        elif L == 4:
            c += 1
            break
        elif L == 3:
            c += 1
            break
        elif L == 2:
            c += 1
            break
        elif L == 1:
            c += 1
            break
    print(c)