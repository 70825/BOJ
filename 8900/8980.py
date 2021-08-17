n, c = map(int, input().split())
m = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(m)], key=lambda x: [x[1], x[0]])
box = [c] * (n + 1)
ans = 0
idx = 1
for i in range(m):
    val = min(arr[i][2], min(box[arr[i][0]:arr[i][1]]))
    for j in range(arr[i][0], arr[i][1]):
        box[j] -= val
    ans += val
print(ans)