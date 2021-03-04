def matching():
    def dfs(x):
        visited[x]=1
        for nx in path[x]:
            if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
                A[x]=nx;B[nx]=x;return 1
        return 0
    A,B,ans=[-1]*n,[-1]*m,0
    for i in range(n):
        if A[i]==-1:
            visited=[0]*n
            if dfs(i):ans+=1
    return ans
n,m,k1,k2=map(int,input().split())
path=[[] for _ in range(n)]
for i in range(k1):
    a,b=map(int,input().split())
    a-=1;b-=1
    path[a].append(b)
x=matching()
path=[[] for _ in range(n)]
for i in range(k2):
    a,b=map(int,input().split())
    a-=1;b-=1
    path[a].append(b)
y=matching()
print(['그만 알아보자','네 다음 힐딱이'][x<y])