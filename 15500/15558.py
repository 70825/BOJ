from collections import deque
N,k=map(int,input().split())
D=[input() for _ in range(2)]
S=[[0]*N for _ in range(2)]
q=deque([(0,0,1)]);S[0][0]=1
while q:
    x,y,z=q.popleft()
    for nx,ny in [(x,y+1),(x,y-1),(x+1,y+k),(x-1,y+k)]:
        if 0<=nx<2 and z<=ny<N and D[nx][ny]=='1' and S[nx][ny]==0:
            q.append((nx,ny,z+1));S[nx][ny]=1
        elif 0<=nx<2 and ny>=N:print(1);exit()
print(0)