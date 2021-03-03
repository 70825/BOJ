n=int(input())
S=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    S[i][i]=0
while 1:
    x,y=map(int,input().split())
    if x==y==-1:break
    S[x][y]=1;S[y][x]=1
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            S[i][j]=min(S[i][j],S[i][k]+S[k][j])
ans=float('inf')
D=[]
for i in range(1,n+1):
    ans=min(ans,max(S[i][1::]))
for i in range(1,n+1):
    k=max(S[i][1::])
    if k==ans:D.append(i)
print(ans,len(D))
print(*D)