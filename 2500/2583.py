from collections import deque
n,m,k=map(int,input().split())
S=[[0]*m for _ in range(n)]
q,dx,dy=deque(),[0,0,1,-1],[1,-1,0,0]
t=0;ans=0;D=[]
for _ in range(k):
    a,b,c,d=map(int,input().split())
    for j in range(a,c):
        for i in range(b,d):S[i][j]=1
for i in range(n):
    for j in range(m):
        if S[i][j]==0:
            q.append((i,j))
            S[i][j]=1;t+=1;ans+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<m and S[nx][ny]==0:
                        ans+=1;S[nx][ny]=1;q.append((nx,ny))
            D.append(ans);ans=0
print(t)
print(' '.join(map(str,sorted(D))))