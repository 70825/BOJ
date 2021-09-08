n = int(input())
w = sorted([*map(int, input().split())])
ans = 987654321
for i in range(n):
    ans = min(ans, w[i] + w[-i-1])
print(ans)