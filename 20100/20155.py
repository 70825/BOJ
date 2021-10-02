input = __import__('sys').stdin.readline

n, m = map(int, input().split())
x = [*map(int, input().split())]
arr = [0] * 1001
for i in range(n):
    arr[x[i]] += 1
print(max(arr))