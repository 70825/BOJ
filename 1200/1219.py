n,s,e,m=map(int,input().split())
D=[[] for _ in range(n)]
S=[float('inf')]*n
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
K=[*map(int,input().split())]
S[s]=-K[s]
for z in range(2):
    for i in range(n):
        for x in range(n):
            for nx,t in D[x]:
                if S[nx]>S[x]+t-K[nx]:
                    S[nx]=S[x]+t-K[nx]
                    if z:S[nx]=-float('inf')
if S[e]==-float('inf'):print('Gee')
elif S[e]==float('inf'):print('gg')
else:print(-S[e])