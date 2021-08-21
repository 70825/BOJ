a, d, k = map(int, input().split())
d /= 100
k /= 100
time = a
ans = d * time
lose = 1-d
while d < 1:
    d *= (1 + k)
    if d > 1: d = 1
    time += a
    ans += lose * d * time
    lose *= 1 - d
print(ans)