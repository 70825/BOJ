input = __import__('sys').stdin.readline
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
sx, sy = map(int, input().split())
up, down, left, right = True, True, True, True #탈출 여부
for i in range(n):
    arr[i][0] -= sx
    arr[i][1] -= sy
for x, y in arr:
    if x >= 0 and y >= 0:
        if x == y: up, right = False, False
        elif min(x, y) == x: up = False
        else: right = False
    if x >= 0 and y <= 0:
        if x == abs(y): right, down = False, False
        elif min(x, abs(y)) == x: down = False
        else: right = False
    if x <= 0 and y >= 0:
        if abs(x) == y: left, up = False, False
        elif min(abs(x), y) == abs(x): up = False
        else: left = False
    if x <= 0 and y <= 0:
        if abs(x) == abs(y): left, down = False, False
        elif min(abs(x), abs(y)) == abs(x): down = False
        else: left = False
if up or down or left or right: print('YES')
else: print('NO')