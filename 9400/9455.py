for i in range(int(input())):
    N,M=map(int,input().split())
    D=[];count=0
    for j in range(N):
        D.append([*map(int,input().split())])
    for j in range(M):
        c=N-1
        for k in range(N-1,-1,-1):
            if D[k][j]==1:count+=c-k;c-=1
    print(count)