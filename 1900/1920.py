input = __import__('sys').stdin.readline

n = int(input())
A = sorted([*map(int,input().split())])
m = int(input())
B = [*map(int,input().split())]

for i in range(m):
    low, high = 0, n-1
    val = B[i]
    res = 0

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == val:
            res = 1
            break
        if A[mid] > val: high = mid - 1
        else: low = mid + 1
    print(res)