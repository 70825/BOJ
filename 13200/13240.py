N,M=map(int,input().split())
A=[[]*M for i in range(N)]
for i in range(N):
    if i%2==0:
        for j in range(M):
            if j%2==0:print('*',end="")
            else:print('.',end="")
    else:
        for j in range(M):
            if j%2==0:print('.',end="")
            else:print('*',end="")
    print("")