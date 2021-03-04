n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
V=[['.']*m for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if D[i][j]=='X':
            ans=0
            for k in range(4):
                x,y=i+dx[k],j+dy[k]
                if 0<=x<n and 0<=y<m and D[x][y]=='.':ans+=1
                elif x>=n or x<0 or y>=m or y<0:ans+=1
            if ans<3:V[i][j]='X'
a,b,c,d=100,100,0,0
for i in range(n):
    for j in range(m):
        if V[i][j]=='X':
            a,c=min(a,i),max(c,i)
            b,d=min(b,j),max(d,j)
for i in range(a,c+1):
    for j in range(b,d+1):print(V[i][j],end='')
    print()