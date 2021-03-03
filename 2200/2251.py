from collections import deque
D=[*map(int,input().split())]
a,b,c=0,0,D[2]
S=[0]*201;S[D[2]]=1
check=[[0]*201 for _ in range(201)];check[0][0]=1
dx,dy=[0,0,1,1,2,2],[1,2,0,2,0,1]
q=deque([(0,0)])
while q:
    x,y=q.popleft()
    z=D[2]-x-y
    for i in range(6):
        water=[x,y,z]
        water[dy[i]]+=water[dx[i]]
        water[dx[i]]=0
        if water[dy[i]]>D[dy[i]]:
            water[dx[i]]=water[dy[i]]-D[dy[i]]
            water[dy[i]]-=water[dx[i]]
        if check[water[0]][water[1]]==0:
            if water[0]==0 and S[water[2]]==0:S[water[2]]=1
            check[water[0]][water[1]]=1
            q.append((water[0],water[1]))
for i in range(201):
    if S[i]==1:print(i,end=" ")