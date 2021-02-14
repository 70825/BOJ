from heapq import *
n,m,k=map(int,input().split())
D=[[] for _ in range(n+1)]
S=[float('INF')]*(n+1);S[k]=0
q=[]
def Dijkstra(G,V,z):
    heappush(q,[0,z])
    while q:
        t,x=heappop(q)
        for j in range(len(G[x])):
            nt,nx=t+D[x][j][1],D[x][j][0]
            if V[nx]>nt:V[nx]=nt;heappush(q,[nt,nx])
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
Dijkstra(D,S,k)
for i in range(1,n+1):
    K=[float('INF')]*(n+1);K[i]=0
    Dijkstra(D,K,i)
    S[i]+=K[k]
print(max(S[1::]))