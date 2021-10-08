h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())
n = int(input())

ans = 0
while 1:
    if n in [h1 // 10, h1 % 10, m1 // 10, m1 % 10]: ans += 1
    if h1 == h2 and m1 == m2: break
    m1 += 1
    if m1 == 60: h1 += 1; m1 = 0
print(ans)