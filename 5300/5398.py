def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if V[nx]==-1 or (not visited[V[nx]] and dfs(V[nx])):
            H[x]=nx
            V[nx]=x
            return 1
    return 0
for __ in range(int(input())):
    h,v=map(int,input().split())
    word=[['.']*(2000) for _ in range(2000)]
    num=[[-1]*(2000) for _ in range(2000)]
    path=[[] for _ in range(h)]
    for i in range(h):
        y,x,z=input().split()
        x,y=int(x),int(y)
        for j in range(len(z)):
            word[x][y+j]=z[j]
            num[x][y+j]=i
    for i in range(v):
        y,x,z=input().split()
        x,y=int(x),int(y)
        for j in range(len(z)):
            if word[x+j][y]!=z[j] and num[x+j][y]!=-1:
                path[num[x+j][y]].append(i)
    H=[-1]*h
    V=[-1]*v
    res=0
    for i in range(h):
        if H[i]==-1:
            visited=[0]*h
            if dfs(i):res+=1
    print(h+v-res)