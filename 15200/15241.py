n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
S=[[0]*m for _ in range(n)];S[0][0]=1
for i in range(1,m):
    if D[0][i]=='.':S[0][i]=S[0][i-1]
    else:break
for i in range(1,n):
    if D[i][0]=='.':S[i][0]=S[i-1][0]
    else:break
for i in range(1,n):
    for j in range(1,m):
        if D[i][j]=='.':S[i][j]=(S[i-1][j]+S[i][j-1])%1000000007
print(S[n-1][m-1])