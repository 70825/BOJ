def F(x):
    if S[x]<0:return x
    S[x]=F(S[x])
    return S[x]
n,m=map(int,input().split())
S=[-1]*(n+1)
D=[];ans=0
for i in range(m):
    a,b,c=map(int,input().split())
    D.append((c,a,b))
D.sort()
for i in range(m):
    if F(D[i][1])!=F(D[i][2]):
        ans+=D[i][0]
        S[F(D[i][1])]=F(D[i][2])
print(ans)