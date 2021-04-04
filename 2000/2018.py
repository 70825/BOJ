n = int(input())
x, y = 0,1
ans = 0
while 1:
    if y == n: break
    res = y*(y+1)//2 - x*(x+1)//2
    if res <= n:
        if res == n:ans += 1
        y += 1
    else: x += 1
print(ans+1)