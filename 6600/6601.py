from collections import deque
dx,dy=[-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]
def C(k):return ord(k[0])-97,int(k[1])-1
while 1:
    try:
        a,b=map(str,input().split())
        sx,sy=C(a);ex,ey=C(b)
        S=[[-1]*8 for _ in range(8)]
        q=deque([(sx,sy)]);S[sx][sy]=0
        while q:
            x,y=q.popleft()
            for i in range(8):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<8 and 0<=ny<8 and S[nx][ny]==-1:
                    q.append((nx,ny));S[nx][ny]=S[x][y]+1
        print('To get from {} to {} takes {} knight moves.'.format(a,b,S[ex][ey]))
    except EOFError:break