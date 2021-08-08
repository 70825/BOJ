input = __import__('sys').stdin.readline
n = int(input())
x = sorted([*map(int, input().split())], reverse=True)
m = int(input())
y = sorted([*map(int, input().split())], reverse=True)
if y[0] > x[0]:
    print(-1)
    exit()
ans = 0
while len(y):
    ans += 1
    for i in range(n):
        for j in range(len(y)):
            if x[i] >= y[j]:
                del y[j]
                break
print(ans)