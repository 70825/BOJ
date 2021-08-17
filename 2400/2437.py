n = int(input())
arr = sorted([*map(int, input().split())])
if arr[0] != 1:print(1);exit()
val = arr[0]
for i in range(1, n):
    if val + 1 < arr[i]:
        print(val + 1)
        exit()
    val += arr[i]
print(val + 1)