def topologySort(x):
    visited[x]=1
    for nx in adj[x]:
        if visited[nx]==0:
            topologySort(nx)
    topology.append(x)
def KosarajuDFS(x,SCC):
    visited[x]=1
    SCC.append(x)
    for nx in radj[x]:
        if visited[nx]==0:
            KosarajuDFS(nx,SCC)
import sys
sys.setrecursionlimit(100000)
input=__import__('sys').stdin.readline
n,t=map(int,input().split())
adj=[[] for _ in range(n)]
radj=[[] for _ in range(n)]
for i in range(t):
    a,b=map(int,input().split())
    a-=1;b-=1
    adj[a].append(b)
    radj[b].append(a)
visited=[0]*n
topology=[]
for i in range(n):
    if visited[i]==0:topologySort(i)
visited=[0]*n
SCC=[]
while topology:
    x = topology.pop()
    if visited[x]==0:
        SCC.append([])
        KosarajuDFS(x,SCC[-1])
for i in range(len(SCC)):
    SCC[i]=sorted(SCC[i])
SCC=sorted(SCC)
print(len(SCC))
for curr in SCC:
    for x in curr:
        print(x+1,end=" ")
    print(-1)