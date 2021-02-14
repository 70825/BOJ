def prime(n):
    s=[True]*(n+1)
    s[0]=False
    s[1]=False
    for i in range(2,int((n)**0.5)+1):
        if s[i]:
            for j in range(i+i,n+1,i):
                s[j]=False
    return s
def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if b[nx]==-1 or (not visited[b[nx]] and dfs(b[nx])):
            a[x]=nx
            b[nx]=x
            return 1
    return 0
Prime=prime(2000)
m=int(input())
D=[*map(int,input().split())]
A=[]
B=[]
for i in range(len(D)):
    if D[i]%2==D[0]%2:A.append(D[i])
    else:B.append(D[i])
if len(A)!=len(B):print(-1);exit(0)
path=[[] for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B)):
        if Prime[A[i]+B[j]]:path[i].append(j)
K=[]
for z in range(len(path[0])):
    a=[-1]*len(A)
    b=[-1]*len(B)
    a[0]=path[0][z]
    b[path[0][z]]=0
    res=1
    for i in range(1,len(A)):
        visited=[0]*len(A);visited[0]=1
        if dfs(i):res+=1
    if res==len(A):K.append(B[path[0][z]])
if len(K)==0:print(-1)
else:print(*sorted(K))