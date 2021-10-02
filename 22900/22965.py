n = int(input())
arr = [*map(int, input().split())]
new_arr = sorted([i for i in range(n)], key=lambda x: arr[x])
val = 1
for i in range(1, n):
    if new_arr[i-1] + 1 != new_arr[i]: val += 1
print(min(val, 3))