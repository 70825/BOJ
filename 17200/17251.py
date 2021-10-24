input = __import__('sys').stdin.readline
n = int(input())
arr = [*map(int, input().split())]
r_max = [0] * (n-1); r_max[0] = arr[0]
b_max = [0] * (n-1); b_max[-1] = arr[-1]
for i in range(1, n-1):
    r_max[i] = max(r_max[i-1], arr[i])
    b_max[-i-1] = max(b_max[-i], arr[-i-1])
r, b = 0, 0
for i in range(n-1):
    if r_max[i] > b_max[i]: r += 1
    if r_max[i] < b_max[i]: b += 1
print('R' if r > b else 'B' if b > r else 'X')