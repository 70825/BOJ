from heapq import *
n=int(input())
D=[[] for _ in range(n+1)]
T,M=map(int,input().split())
S=[[float('inf')]*(T+1) for _ in range(n+1)];S[1][0]=0
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    D[a].append((b,c,d))
    D[b].append((a,c,d))
q=[];heappush(q,(0,0,1))
while q:
    c,t,x=heappop(q)
    if S[x][t]!=c:continue
    for nx,nt,nc in D[x]:
        if 0<=t+nt<=T and 0<=c+nc<=M and S[nx][nt+t]>nc+c:
            S[nx][nt+t]=nc+c;heappush(q,[nc+c,nt+t,nx])
ans=min(S[n])
print([ans,-1][ans==float('inf')])