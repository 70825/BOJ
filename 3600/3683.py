def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if A[nx]==-1 or (not visited[A[nx]] and dfs(A[nx])):
            A[nx]=x
            return 1
    return 0
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    c,d,v=map(int,input().split())
    win=[]
    lose=[]
    path=[[] for _ in range(v)]
    for i in range(v):
        a,b=input().strip().split()
        win.append(a)
        lose.append(b)
    for i in range(v):
        for j in range(i+1,v):
            if win[i]==lose[j] or lose[i]==win[j]:
                if win[i][0]=='C':path[i].append(j)
                else:path[j].append(i)
    A=[-1]*v
    res=0
    for i in range(v):
        if A[i]==-1:
            visited=[0]*v
            if (dfs(i)):res+=1
    print(v-res)