from collections import deque
D=[list(map(str,input().split())) for _ in range(3)]
k=''
for i in range(3):
    for j in range(3):
        k+=D[i][j]
q=deque([k])
S={k:0}
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    puzzle=q.popleft()
    z=puzzle.find('0')
    x,y=z//3,z%3
    for i in range(4):
        nx,ny,puz=x+dx[i],y+dy[i],[*puzzle]
        if 0<=nx<3 and 0<=ny<3:
            puz[3*nx+ny],puz[3*x+y]=puz[3*x+y],puz[3*nx+ny]
            pp=''.join(puz)
            if pp not in S:
                S[pp]=S[puzzle]+1;q.append(pp)
if '123456780' in S:print(S['123456780'])
else:print(-1)