def dfs(x,y,z):
    global ans
    if x==n-1 and y==n-1:ans+=1;return
    if z in [0,1] and y+1<n and D[x][y+1]==0:dfs(x,y+1,0)
    if z in [0,1,2] and x+1<n and y+1<n and D[x+1][y]==D[x][y+1]==D[x+1][y+1]==0:dfs(x+1,y+1,1)
    if z in [1,2] and x+1<n and D[x+1][y]==0:dfs(x+1,y,2)
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
ans=0
dfs(0,1,0)
print(ans)