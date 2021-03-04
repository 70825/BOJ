from collections import deque
a,b,c=map(int,input().split())
z=a+b+c
if (a+b+c)%3!=0:print(0);exit()
D=[[0]*(z+1) for _ in range(z+1)]
D[min(a,b,c)][max(a,b,c)]=1;q=deque([(a,b,c)])
while q:
    a,b,c=q.popleft()
    if a==b==c:print(1);exit()
    for nx,ny in [(a,b),(a,c),(b,c)]:
        if nx<ny:nx,ny=ny,nx
        nx,ny,nz=nx-ny,2*ny,z-nx-ny
        Min,Max=min(nx,ny,nz),max(nx,ny,nz)
        if D[Min][Max]==0:
            q.append((nx,ny,nz));D[Min][Max]=1
print(0)