def edge(x,y,z):
    path[x].append(y)
    path[y].append(x)
    c[x][y]=z
from collections import deque
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n=int(input())
    nm=2*(n+1)
    S=nm-2;E=S+1
    soldier=0
    c=[[0]*nm for _ in range(nm)]
    path=[[] for _ in range(nm)]
    enemy=[0]*n
    D=[*map(int,input().split())]
    for i in range(n):
        if D[i]>0:
            edge(S,i,D[i])
            edge(i+n,E,1)
            edge(i,i+n,100000)
            soldier+=1
    for i in range(n):
        K=input()
        if D[i]!=0:
            for j in range(len(K)):
                if K[j]=='Y':
                    if D[j]!=0:edge(i,n+j,100000)
                    else:enemy[i]=1
    l,r=0,sum(D)+1
    res=0
    while l<=r:
        m=(l+r)//2
        f=[[0]*nm for _ in range(nm)]
        for i in range(n):
            if enemy[i]==1:c[i+n][E]=m
            if enemy[i]==0 and D[i]>0:c[i+n][E]=1
        ALL=soldier-sum(enemy)+sum(enemy)*m
        ans=0
        while 1:
            prev=[-1]*nm
            q=deque([S])
            while q:
                x=q.popleft()
                for nx in path[x]:
                    if c[x][nx]-f[x][nx]>0 and prev[nx]==-1:
                        prev[nx]=x;q.append(nx)
            if prev[E]==-1:break
            flow=float('inf')
            x=E
            while x!=S:
                nx=prev[x]
                flow=min(flow,c[nx][x]-f[nx][x])
                x=nx
            x=E
            while x!=S:
                nx=prev[x]
                f[nx][x]+=flow
                f[x][nx]-=flow
                x=nx
            ans+=flow
        if ans==ALL:l=m+1;res=max(res,m)
        else:r=m-1
    print(res)