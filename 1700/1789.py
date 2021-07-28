x = int(input()) * 2
ans = 0
for i in range(1, 1000000):
    ans = i * i + i
    if ans >= x: break
print([i - 1, i][ans == x])