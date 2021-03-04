def go():
    S[i][j][0]=S[i][j-1][0]+S[i][j-1][1]
    S[i][j][2]=S[i-1][j][1]+S[i-1][j][2]
    if D[i-1][j]==D[i][j-1]==0:S[i][j][1]=sum(S[i-1][j-1])
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
S=[[[0]*3 for _ in range(n)] for __ in range(n)]
S[0][1][0]=1
for i in range(2,n):
    if D[0][i]==1:break
    S[0][i][0]=1
for i in range(1,n):
    for j in range(2,n):
        if D[i][j]==0:go()
print(sum(S[n-1][n-1]))