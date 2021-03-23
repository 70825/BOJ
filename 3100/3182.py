n = int(input())
adj = []
ans = [-1, 0]
for i in range(n):
    x = int(input())
    adj.append(x-1)
for i in range(n):
    q = [i]
    visit = [0]*n
    visit[i] = 1
    while 1:
        if visit[adj[q[-1]]]: break
        visit[adj[q[-1]]] = 1
        q.append(adj[q[-1]])
    if ans[1] < len(q):
        ans = [i+1, len(q)]
print(ans[0])