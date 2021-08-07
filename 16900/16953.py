A, B = map(int, input().split())
q = __import__('collections').deque([[A, 0]])

while q:
    x, y = q.popleft()
    if x == B:
        print(y + 1)
        exit()
    arr = [2 * x, int(str(x) + '1')]
    for nx in arr:
        if nx <= B:
            q.append([nx, y+1])
print(-1)