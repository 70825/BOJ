for _ in range(int(input())):
    N=int(input())
    a=[0]+[*map(int,input().split())]
    b=[0]+[*map(int,input().split())]
    S=[*zip(a,b)]
    D=[[0]*3 for __ in range(N+1)]
    for i in range(1,N+1):
        D[i][0]=max(D[i-1])
        D[i][1]=max(D[i-1][0],D[i-1][2])+S[i][0]
        D[i][2]=max(D[i-1][0],D[i-1][1])+S[i][1]
    print(max(D[N]))