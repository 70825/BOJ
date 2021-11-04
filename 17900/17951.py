n, k = map(int, input().split())
arr = [*map(int, input().split())]
s, e = 0, sum(arr)
while s <= e:
    mid = (s + e) // 2
    val = 0
    count = 0
    for i in range(n):
        if val + arr[i] >= mid:
            count += 1
            val = 0
        else: val += arr[i]

    if count >= k: s = mid + 1
    else: e = mid - 1
print(e)