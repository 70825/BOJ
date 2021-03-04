input=__import__('sys').stdin.readline
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if D[i][k]==1 and D[k][j]==1:D[i][j]=1
for i in range(n):
    print(*D[i])