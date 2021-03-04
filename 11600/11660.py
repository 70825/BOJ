input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
P=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        P[i+1][j+1]=P[i+1][j]+P[i][j+1]-P[i][j]+D[i][j]
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(P[x2][y2]-P[x2][y1-1]-P[x1-1][y2]+P[x1-1][y1-1])