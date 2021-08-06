input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = sorted([[*map(int, input().split())] for _ in range(n)])
    val = arr[0][1]
    ans = 1
    for i in range(1, n):
        if val > arr[i][1]:
            ans += 1
            val = arr[i][1]
    print(ans)