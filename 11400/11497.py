for _ in range(int(input())):
    n = int(input())
    arr = sorted([*map(int,input().split())])
    D = [0] * n
    for i in range(0, n, 2):
        D[i//2] = arr[i]
    for i in range(1, n, 2):
        D[-(i//2)-1] = arr[i]
    ans = abs(D[0] - D[-1])
    for i in range(1, n):
        ans = max(ans, abs(D[i] - D[i-1]))
    print(ans)