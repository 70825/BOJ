from collections import deque
input=__import__('sys').stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    D=[[] for __ in range(n+1)]
    S=[0]*(n+1);t=0
    for i in range(m):
        a,b=map(int,input().split())
        D[a].append(b);D[b].append(a)
    q=deque([1]);S[1]=1
    while q:
        x=q.popleft()
        for i in range(len(D[x])):
            if S[D[x][i]]==0:S[D[x][i]]=1;q.append(D[x][i]);t+=1
    print(t)