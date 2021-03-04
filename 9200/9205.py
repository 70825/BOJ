from collections import deque
for _ in range(int(input())):
    n = int(input())
    store = [[*map(int,input().split())] for _ in range(n+2)]
    adj = [[] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            x1,y1 = store[i]
            x2,y2 = store[j]
            if abs(x1-x2) + abs(y1-y2) <= 1000:
                adj[i].append(j)
                adj[j].append(i)
    S = [0]*(n+2);S[0] = 1
    q = deque([0])
    while q:
        t = q.popleft()
        for nt in adj[t]:
            if S[nt] == 0:
                S[nt] = 1
                q.append(nt)
    print(['sad','happy'][S[n+1]])