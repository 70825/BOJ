n, x = map(int, input().split())
C = sorted([*map(int, input().split())])
ans = 0
for i in range(n-1, -1, -1):
    if C[i] == x: C.pop(); ans += 1
    else: break
s, e = 0, len(C) - 1
etc = 0
while s <= e:
    if s == e: etc += 1; break
    if 2 * (C[s] + C[e]) >= x:
        s += 1
        e -= 1
        ans += 1
    else:
        etc += 1
        s += 1
print(ans + etc // 3)