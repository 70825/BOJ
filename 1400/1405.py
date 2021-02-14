def go(x,y,t,pp):
    global ans,z
    if z==0:ans+=t;return
    for i in range(4):
        if (pp==0 and i==1) or (pp==1 and i==0) or (pp==2 and i==3) or (pp==3 and i==2):continue
        nx,ny=x+dx[i],y+dy[i]
        if check[nx][ny]==0:
            z-=1;check[nx][ny]=1
            go(x+dx[i],y+dy[i],(t*D[i]/100),i)
            z+=1;check[nx][ny]=0
dx,dy=[0,0,1,-1],[-1,1,0,0]#동서남북
z,*D=map(int,input().split())
check=[[0]*30 for _ in range(30)];check[15][15]=1
ans=0
for i in range(4):
    nx,ny=15+dx[i],15+dy[i]
    check[nx][ny]=1;z-=1
    go(nx,ny,D[i]/100,i)
    check[nx][ny]=0;z+=1
print(ans)