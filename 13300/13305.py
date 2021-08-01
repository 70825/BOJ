n = int(input())
road = [*map(int, input().split())]
city = [*map(int, input().split())]

oil = city[0]
ans = 0

for i in range(1, n):
    ans += road[i-1] * oil
    if city[i] < oil: oil = city[i]

print(ans)