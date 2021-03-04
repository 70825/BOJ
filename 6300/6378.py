while 1:
    N=str(input())
    if N=='0':break
    while len(N)!=1:
        k=0
        for i in range(len(N)):k+=int(N[i])
        N=str(k)
    print(N)