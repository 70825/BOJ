n, l = map(int, input().split())
h = sorted([*map(int, input().split())])
for i in range(n):
    if l + i < h[i]:
        print(l + i); exit()
print(l + n)