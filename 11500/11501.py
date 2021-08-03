input = __import__('sys').stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [*map(int, input().split())]

    ans = 0
    val = arr[-1]
    for i in range(n-1, -1, -1):
        if arr[i] <= val: ans += val - arr[i]
        else: val = arr[i]
    print(ans)