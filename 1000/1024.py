n, l = map(int, input().split())
for i in range(l, 101):
    s = i * (i + 1) // 2 - i
    if n >= s and (n - s) % i == 0:
        arr = [j + (n-s)//i for j in range(i)]
        print(*arr); exit()
print(-1)