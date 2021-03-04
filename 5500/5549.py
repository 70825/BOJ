input=__import__('sys').stdin.readline
n,m=map(int,input().split())
k=int(input())
D=[[*input().strip()] for _ in range(n)]
pSum=[[[0]*3 for __ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        for l in range(3):
            pSum[i+1][j+1][l]=pSum[i+1][j][l]+pSum[i][j+1][l]-pSum[i][j][l]
        if D[i][j]=='J':pSum[i+1][j+1][0]+=1
        elif D[i][j]=='O':pSum[i+1][j+1][1]+=1
        else:pSum[i+1][j+1][2]+=1
for i in range(k):
    a,b,c,d=map(int,input().split())
    ans=[0,0,0]
    for j in range(3):
        ans[j]=pSum[c][d][j]-pSum[a-1][d][j]-pSum[c][b-1][j]+pSum[a-1][b-1][j]
    print(*ans)