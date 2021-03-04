from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
for ___ in range(int(input())):
    n,m=map(int,input().split())
    n+=2;m+=2
    D=['.'*m]+['.'+input()+'.' for _ in range(n-2)]+['.'*m]
    Key=input()
    S=[[0]*m for _ in range(n)]
    Kq=[[] for _ in range(26)]
    Document=0
    q=deque([(0,0)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='*' and S[nx][ny]==0:
                if 65<=ord(D[nx][ny])<=90:
                    if chr(ord(D[nx][ny])+32) in Key:q.append((nx,ny));S[nx][ny]=1
                    else:Kq[ord(D[nx][ny])-65].append((nx,ny));S[nx][ny]=1
                elif 97<=ord(D[nx][ny])<=122:
                    q.append((nx,ny));S[nx][ny]=1;Key+=D[nx][ny]
                    z=ord(D[nx][ny])-97
                    for j in range(len(Kq[z])):
                        q.append(Kq[z][j])
                    Kq[z]=[]
                elif D[nx][ny]=='$':Document+=1;q.append((nx,ny));S[nx][ny]=1
                else:S[nx][ny]=1;q.append((nx,ny))
    print(Document)