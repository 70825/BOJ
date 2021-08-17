def go(x, y):
    arr[x][y] = 'x'
    if y == c - 1: return 1
    for nx in [x-1, x, x+1]:
        if 0 <= nx < r and arr[nx][y+1] == '.' and go(nx, y+1): return 1
    return 0

input = __import__('sys').stdin.readline
r, c = map(int, input().split())
arr = [[*input().strip()] for _ in range(r)]
print(sum(go(i, 0) for i in range(r)))