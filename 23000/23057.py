def go(x):
    if x == n:
        res = sum(arr[i] for i in range(len(check)) if check[i])
        val[res] = 1
        return
    check[x] = 1
    go(x+1)
    check[x] = 0
    go(x+1)

n = int(input())
arr = [*map(int, input().split())]
total = sum(arr)
val = __import__('collections').defaultdict(lambda : 0)
check = [0] * len(arr)
go(0)

ans = sum(1 for x in val.keys() if val[x])
print(total - ans + 1)