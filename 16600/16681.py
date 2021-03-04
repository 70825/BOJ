from heapq import *
input=__import__('sys').stdin.readline
n,m,d,e=map(int,input().split())
K=[0]+[*map(int,input().split())]
D=[[] for _ in range(n+1)]
ans=-float('INF')
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
    D[b].append((a,c))
def Dijkstra(G,A):
    G[A]=0
    q=[];heappush(q,[0,A])
    while q:
        t,x=heappop(q)
        if G[x]!=t:continue
        for nx,nt in D[x]:
            if K[nx]>K[x] and G[nx]>nt+t:
                G[nx]=nt+t;heappush(q,[nt+t,nx])
X=[float('INF')]*(n+1)
Dijkstra(X,1)
Y=[float('INF')]*(n+1)
Dijkstra(Y,n)
for i in range(1,n+1):
    k=K[i]*e-(X[i]+Y[i])*d
    if k>ans:ans=k
print([ans,'Impossible'][ans==-float('INF')])