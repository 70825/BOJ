input=__import__('sys').stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    if 100*c+d < 301 or 100*a+b > 1130: continue
    arr.append([100*a+b, 100*c+d])
arr.sort()
flower = [-1, -1]
idx = -1
for i in range(n):
    if arr[i][0] > 301: break
    if arr[i][1] > flower[1]:
        flower = arr[i]
        idx = i
ans = 1
day = flower[1]
while day <= 1130:
    next_flower = [-1, -1]
    for i in range(idx, n):
        if arr[i][0] > day: break
        if flower[0] < arr[i][0] <= flower[1] < arr[i][1]:
            if arr[i][1] > next_flower[1]:
                next_flower = arr[i]
                idx = i
    if next_flower[0] == -1:
        print(0)
        exit()
    flower = next_flower
    day = flower[1]
    ans += 1
print(ans)
