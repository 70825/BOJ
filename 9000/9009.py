for _ in range(int(input())):
    n = int(input())
    ans = []
    while n != 0:
        arr = [0, 1]
        while arr[1] <= n:
            arr = arr[1], sum(arr)
        if arr[1] == n:
            ans.append(arr[1])
            n -= arr[1]
        else:
            ans.append(arr[0])
            n -= arr[0]
    print(' '.join(map(str, sorted(ans))))