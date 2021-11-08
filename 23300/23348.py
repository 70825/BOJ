a, b, c = map(int, input().split())
n = int(input())
arr = [0] * n
for i in range(3 * n):
    idx = i // 3
    x, y, z = map(int, input().split())
    arr[idx] += x * a + y * b + z * c
print(max(arr))