while 1:
    S=str(input());d=0
    if S=='#':break
    for i in range(len(S)):
        if S[i]==' ':
            d+=0
        else:
            d+=(ord(S[i])-64)*(i+1)
    print(d)