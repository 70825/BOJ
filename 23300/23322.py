input = __import__('sys').stdin.readline

n, k = map(int, input().split())
arr = [*map(int, input().split())]
ans = 0
time = 0
while max(arr) != 1:
    flag = False
    for i in range(k, n):
        if arr[i-k] != arr[i]:
            ans += arr[i] - arr[i-k]
            arr[i] = arr[i-k]
            time += 1
            arr.sort()
            flag = True
            break
    if not flag: break
print(ans, time)