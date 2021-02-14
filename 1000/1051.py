n,m=map(int,input().split())
D = [input() for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(j,m):
                x = i + k - j
                if x < n and D[i][j] == D[i][k] == D[x][j] == D[x][k]:
                    ans = max(ans, (x-i+1)*(k-j+1))
print(ans)