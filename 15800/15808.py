import heapq
input=__import__('sys').stdin.readline
MIS = lambda: map(int,input().split())
n=int(input())
D=[[] for _ in range(n+1)]
for i in range(n):
    for j,z in enumerate(MIS()):
        if z!=0:D[i+1].append((j+1,z))
S=[float('INF')]*(n+1)
w,u=MIS()
q=[]
for i in range(w):
    X,T=MIS()
    S[X]=-T
    heapq.heappush(q,[S[X],X])
while q:
    t,x=heapq.heappop(q)
    if S[x]!=t:continue
    for nx,nt in D[x]:
        if S[nx]>t+nt:
            S[nx]=t+nt;heapq.heappush(q,[S[nx],nx])
resort=[tuple(MIS()) for i in range(u)]
print(max(c-S[a] for a,c in resort))