from heapq import *
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,d,c=map(int,input().split())
    S=[float('inf')]*(n+1)
    D=[[] for _ in range(n+1)]
    for i in range(d):
        a,b,s=map(int,input().split())
        D[b].append((a,s))
    q=[];heappush(q,(0,c));S[c]=0
    while q:
        t,x=heappop(q)
        if S[x]!=t:continue
        for nx,nt in D[x]:
            if S[nx]>nt+t:
                S[nx]=nt+t;heappush(q,(nt+t,nx))
    ans=0;Max=0
    for i in range(1,n+1):
        if S[i]!=float('inf'):
            ans+=1;Max=max(Max,S[i])
    print(ans,Max)