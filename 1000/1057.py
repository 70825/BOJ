n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
ans = 1
while 1:
    if (a == 1 and b == 2) or (b % 2 == 0 and a + 1 == b): break
    ans += 1
    a = a // 2 + (1 if a % 2 else 0)
    b = b // 2 + (1 if b % 2 else 0)
print(ans)