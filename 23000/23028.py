def go(x, major, total):
    if x + n == 8:
        if major >= 66 and total >= 130: print('Nice'); exit()
        return
    for i in range(arr[x][0] + 1):
        non_major = min(6 - i, arr[x][1])
        go(x+1, major + 3*i, total + (i + non_major) * 3)

n, a, b = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(10)]
go(0, a, b)
print('Nae ga wae')