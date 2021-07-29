n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])

time = 0
for i in range(n):
    x, y = arr[i]
    if time < x: time = x
    time += y
print(time)