n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr = sorted(arr, key=lambda x:[-x[0],x[1]])

ans = 0
for i in range(5,len(arr)):
    if arr[4][0] == arr[i][0]:
        ans += 1
print(ans)