def F(x):
    if S[x]<0:return x
    S[x]=F(S[x])
    return S[x]
n=int(input())
S=[-1]*n;ans=0;D=[];cnt=0
K=[[*map(int,input().split())] for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        D.append((K[i][j],i,j))
D.sort()
for i in range(len(D)):
    if F(D[i][1])!=F(D[i][2]):
        S[F(D[i][1])]=F(D[i][2])
        ans+=D[i][0];cnt+=1
        if cnt==n-1:break
print(ans)