def F(x):
    if S[x]<0:return x
    S[x]=F(S[x])
    return S[x]
n=int(input())
S=[-1]*(n+1);D=[]
for i in range(int(input())):
    a,b,c=map(int,input().split())
    D.append((c,a,b))
D.sort()
ans=0;cnt=0
for i in range(len(D)):
    if F(D[i][1])!=F(D[i][2]):
        S[F(D[i][1])]=F(D[i][2])
        ans+=D[i][0]
print(ans)