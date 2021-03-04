D=[input() for _ in range(5)]
dx,dy=[2,2,1,1,-1,-1,-2,-2],[1,-1,2,-2,2,-2,1,-1]
ans=0
def K(i,j):
    global ans
    for k in range(8):
        nx,ny=i+dx[k],j+dy[k]
        if 0<=nx<5 and 0<=ny<5 and D[nx][ny]=='k':ans-=1
for i in range(5):
    for j in range(5):
        if D[i][j]=='k':ans+=1;K(i,j)
print(['invalid','valid'][ans==9])