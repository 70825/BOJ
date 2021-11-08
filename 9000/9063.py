min_x = min_y = float('inf')
max_x = max_y = 0

for i in range(int(input())):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
print((max_x - min_x) * (max_y - min_y))