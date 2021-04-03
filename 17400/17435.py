input = __import__('sys').stdin.readline
n = int(input())
max_p = 19
D = [*map(int,input().split())]
parent = [[-1]*max_p for _ in range(n)]

for i in range(n):
    parent[i][0] = D[i]-1
for j in range(max_p-1):
    for i in range(n):
        parent[i][j + 1] = parent[parent[i][j]][j]
for _ in range(int(input())):
    n,x = map(int,input().split()); x-=1
    for j in range(max_p-1,-1,-1):
        if n >= 2**j:
            n -= 2**j
            x = parent[x][j]
    print(x+1)