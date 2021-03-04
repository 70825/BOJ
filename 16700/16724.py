n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
S=[[-1]*m for _ in range(n)]
ans=0;t=0
def a(x,y,k):
    if k=='U':return x-1,y
    if k=='D':return x+1,y
    if k=='L':return x,y-1
    else:return x,y+1
def k(x,y):
    global t,ans
    nx,ny=a(x,y,D[x][y])
    if 0<=nx<n and 0<=ny<m:
        if S[nx][ny]==-1:S[nx][ny]=t;k(nx,ny)
        elif S[nx][ny]==t:ans+=1;return
        else:return
for i in range(n):
    for j in range(m):
        if S[i][j]==-1:S[i][j]=t;k(i,j);t+=1
print(ans)