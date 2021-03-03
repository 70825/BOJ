input = __import__('sys').stdin.readline

def go(x):
    for nx,nt in D[x]:
        if not visit[nx]:
            visit[nx] = 1
            go(nx)
        for i in range(1,n):
            need[x][i] += need[nx][i]*nt

n = int(input())
m = int(input())
D = [[] for _ in range(n+1)]
visit = [0]*(n+1);visit[n] = 1
need = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y,k = map(int,input().split())
    D[x].append([y,k])
for i in range(1,n):
    if len(D[i]) == 0:
        need[i][i] = 1
        visit[i] = 1
go(n)
for i in range(1,n):
    if need[n][i] != 0:
        print(i,need[n][i])