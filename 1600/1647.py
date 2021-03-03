def F(x):
    if S[x]<0:return x
    S[x]=F(S[x])
    return S[x]
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[]
S=[-1]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    D.append((c,a,b))
D.sort()
ans=0;cnt=0
for i in range(len(D)):
    if F(D[i][1])!=F(D[i][2]):
        S[F(D[i][1])]=F(D[i][2])
        ans+=D[i][0];cnt+=1
        if cnt==n-2:break
print(ans)