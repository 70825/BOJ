from heapq import *
input=__import__('sys').stdin.readline
dx,dy=[0,0,1,-1],[1,-1,0,0];Max=float('INF')
for __ in range(int(input())):
    k,m,n=map(int,input().split())
    K=[0]*26;q=[];T=Max
    for i in range(k):
        a,b=map(str,input().split())
        K[ord(a)-65]=int(b)
    D=[input().rstrip() for _ in range(n)]
    S=[[Max]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if D[i][j]=='E':heappush(q,(0,i,j));S[i][j]=0
    while q:
        z,x,y=heappop(q)
        if x in [0,n-1] or y in [0,m-1]:print(S[x][y]);break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and S[nx][ny]>S[x][y]+K[ord(D[nx][ny])-65]:
                S[nx][ny]=S[x][y]+K[ord(D[nx][ny])-65];heappush(q,(S[nx][ny],nx,ny))