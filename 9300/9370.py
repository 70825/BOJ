from heapq import *
input=__import__('sys').stdin.readline
for __ in range(int(input().strip())):
    n,m,k=map(int,input().split())
    s,g,h=map(int,input().split())
    D=[[] for _ in range(n+1)]
    for i in range(m):
        a,b,d=map(int,input().split())
        if (a==g and b==h) or (a==h and b==g):
            D[a].append([b,d-0.5])
            D[b].append([a,d-0.5])
        else:
            D[a].append([b,d])
            D[b].append([a,d])
    S=[float('INF')]*(n+1);S[s]=0
    q=[];heappush(q,[0,s])
    while q:
        t,x=heappop(q)
        if S[x]!=t:continue
        for nx,nt in D[x]:
            if S[nx]>nt+t:
                S[nx]=nt+t;heappush(q,[nt+t,nx])
    K=[]
    for i in range(k):
        z=int(input())
        if S[z]!=float('inf') and S[z]!=int(S[z]):K.append(z)
    print(' '.join(map(str,sorted(K))))