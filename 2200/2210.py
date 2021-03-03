dx,dy=[0,0,1,-1],[1,-1,0,0]
D=[[*map(str,input().split())] for _ in range(5)]
S=[]
def BackTracking(ans,x,y):
    if len(ans)==6:
        if ans not in S:
            S.append(ans)
            return
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<5 and 0<=ny<5 and len(ans)<=5:
            BackTracking(ans+D[nx][ny],nx,ny)
for i in range(5):
    for j in range(5):
        BackTracking(D[i][j],i,j)
print(len(S))