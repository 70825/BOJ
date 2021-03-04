def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if A[nx]==-1 or (not visited[A[nx]] and dfs(A[nx])):
            A[nx]=x
            return 1
    return 0
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
win=[]
lose=[]
path=[[] for _ in range(k)]
for i in range(k):
    a,b,c=map(int,input().split())
    if c==0:
        win.append('B'+str(a))
        lose.append('G'+str(b))
    else:
        win.append('G'+str(b))
        lose.append('B'+str(a))
for i in range(k):
    for j in range(i+1,k):
        if win[i]==lose[j] or win[j]==lose[i]:
            if win[i][0]=='B':path[i].append(j)
            else:path[j].append(i)
res=0
A=[-1]*k
for i in range(k):
    if A[i]==-1:
        visited=[0]*k
        if dfs(i):res+=1
print(res)