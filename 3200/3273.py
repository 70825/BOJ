n = int(input())
D = sorted([*map(int,input().split())])
x = int(input())
a, b = 0, len(D)-1
ans = 0
if D[a]+D[b] > x:
    while 1:
        if D[a]+D[b] <= x: break
        b -= 1
while a < b:
    if D[a]+D[b] <= x:
        if D[a]+D[b] == x: ans += 1
        a += 1
    else:b -= 1
print(ans)