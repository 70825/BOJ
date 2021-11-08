input = __import__('sys').stdin.readline

n, m, l = map(int, input().split())
arr = sorted([int(input()) for i in range(m)])
for i in range(n):
    x = int(input())
    s, e = 0, l
    res = 0
    while s <= e:
        count = 0
        mid = (s+e) // 2
        val = 0
        for j in range(m):
            if arr[j] - val >= mid:
                val = arr[j]
                count += 1
        if l - val >= mid: count += 1
        if count > x:
            res = max(res, mid)
            s = mid + 1
        else:
            e = mid - 1
    print(res)