n, k = map(int, input().split())
v = sorted([*map(int, input().split())])
ans = 1e18
for i in range(1, n):
    team1 = v[0] * i
    team2 = v[i] * (n - i)
    z = team1 + team2
    ans = min(ans, k // z if k % z == 0 else k // z + 1)
print(ans)