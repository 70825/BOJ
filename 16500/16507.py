input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
pSum=[[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        pSum[i+1][j+1]=pSum[i][j+1]+pSum[i+1][j]-pSum[i][j]+D[i][j]
for i in range(k):
    x1,y1,x2,y2=map(int,input().split())
    print((pSum[x2][y2]-pSum[x1-1][y2]-pSum[x2][y1-1]+pSum[x1-1][y1-1])//((x2-x1+1)*(y2-y1+1)))