n,m=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(n)]
S=[[0]*m for _ in range(n)]
S[0][0]=D[0][0]
for i in range(1,m):S[0][i]=S[0][i-1]+D[0][i]
for i in range(1,n):S[i][0]=S[i-1][0]+D[i][0]
for i in range(1,n):
    for j in range(1,m):
        S[i][j]=max(S[i-1][j],S[i][j-1])+D[i][j]
print(S[n-1][m-1])