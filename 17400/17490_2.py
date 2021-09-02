input = __import__('sys').stdin.readline
n, m, k = map(int, input().split())
S = [*map(int, input().split())]
adj = [[] for _ in range(n)]
team = []
stone = []
visit = [0] * n
for i in range(n):
    adj[i].append((i+1)%n)
    adj[(i+1)%n].append(i)
for i in range(m):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    adj[x].remove(y)
    adj[y].remove(x)
for i in range(n):
    if not visit[i]:
        team.append([])
        q = __import__('collections').deque([i])
        visit[i] = 1
        stone.append(S[i])
        while q:
            x = q.popleft()
            for nx in adj[x]:
                if not visit[nx]:
                    visit[nx] = 1
                    q.append(nx)
                    stone[-1] = min(stone[-1], S[nx])
if len(stone) == 1 or sum(stone) <= k: print('YES')
else: print('NO')