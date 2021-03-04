n,m=map(int,input().split())
S=[float('inf')]*(n+1)
D=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
S[1]=0;ans=0
for i in range(1,n+2):
    for j in range(1,n+1):
        for x,t in D[j]:
            if S[x] > S[j]+t:
                S[x]=S[j]+t
                if i==n+1:ans=1
if ans==1:print(-1)
else:
    for i in range(2,n+1):
        print(-1 if S[i]==float('inf') else S[i])