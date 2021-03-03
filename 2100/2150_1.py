def DFS(x):
    global cnt, SN
    cnt+=1
    dfsn[x] = cnt
    S.append(x)
    res = dfsn[x]
    for nx in adj[x]:
        if dfsn[nx]==0: res = min(res,DFS(nx))
        elif finished[nx]==0:res = min(res,dfsn[nx])
    if res==dfsn[x]:
        currSCC=[]
        while 1:
            t = S.pop()
            currSCC.append(t)
            finished[t]=1
            sn[t]=SN
            if t==x:break
        currSCC=sorted(currSCC)
        SCC.append(currSCC)
        SN+=1
    return res
import sys
sys.setrecursionlimit(10**6)
input=__import__('sys').stdin.readline
v,e=map(int,input().split())
adj=[[] for _ in range(v)]
finished=[0]*v
SCC=[]
S=[]
dfsn=[0]*v
sn=[0]*v
cnt,SN=0,0
for i in range(e):
    a,b=map(int,input().split())
    adj[a-1].append(b-1)
for i in range(v):
    if dfsn[i]==0:DFS(i)
SCC=sorted(SCC)
print(SN)
for currSCC in SCC:
    for curr in currSCC:print(curr+1,end=" ")
    print(-1)