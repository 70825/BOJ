while 1:
    n=int(input())
    if n==0:break
    D=[list(map(str,[*input()])) for _ in range(n)]
    S=[list(map(str,[*input()])) for _ in range(n)]
    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if D[i][j]=='O':print(S[i][j],end="")
        D=[*zip(*D[::-1])]
    print()