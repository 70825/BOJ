n,m=map(int,input().split())
A,B=[1]*n,[1]*m
D=[[*map(str,[*input()])] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if D[i][j]=='X':A[i],B[j]=0,0
print([sum(A),sum(B)][sum(B)>sum(A)])