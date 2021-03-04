from collections import deque
F,S,G,U,D=map(int,input().split())
d=[-1]*(F+1);d[S]=0
s=[[-1,-1] for _ in range(F+1)];s[S][0],s[S][1]=0,0
q=deque([(S,0),(S,1)])
dx=[U,-D]
while q:
    x,z=q.popleft()
    for i in range(2):
        nx=x+dx[i]
        for j in range(2):
            if 0<nx<=F and s[nx][i]==-1:q.append((nx,i));s[nx][i]=s[x][z]+1
if s[G][0]==s[G][1]==-1:print('use the stairs')
elif s[G][0]==-1 and s[G][1]!=-1:print(s[G][1])
elif s[G][0]!=-1 and s[G][1]==-1:print(s[G][0])
else:print(min(s[G][0],s[G][1]))