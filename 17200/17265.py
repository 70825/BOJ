def go(x, y, stack):
    global ans
    if x == y == n - 1:
        val = stack[0]
        for i in range(1, len(stack), 2):
            if stack[i] == '+': val += int(stack[i+1])
            if stack[i] == '-': val -= int(stack[i+1])
            if stack[i] == '*': val *= int(stack[i+1])
        ans = [max(ans[0], val), min(ans[1], val)]
    for i in range(2):
        nx, ny = x+dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
            if len(stack) % 2: stack.append(arr[nx][ny])
            else: stack.append(int(arr[nx][ny]))
            visit[nx][ny] = 1
            go(nx, ny, stack)
            stack.pop()
            visit[nx][ny] = 0

dx, dy = [1, 0], [0, 1]
n = int(input())
arr = [[*input().split()] for _ in range(n)]
visit = [[0] * n for _ in range(n)]; visit[0][0] = 1
ans = [-float('inf'), float('inf')]
go(0, 0, [int(arr[0][0])])
print(*ans)