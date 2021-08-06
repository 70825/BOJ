n = int(input())
arr = [*map(int, input().split())]
x = min(arr[0], arr[5])
y = min(arr[1], arr[4])
z = min(arr[2], arr[3])

if n == 1: print(sum(sorted(arr)[:5]))
else:print(4 * (x + y + z) + (8 * n - 12) * min(x + y, y + z, z + x) + (5 * n * n - 16 * n + 12) * min(arr))