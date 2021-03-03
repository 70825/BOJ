from collections import deque
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
Land = [-1]*n
D=[[] for _ in range(n)]
check=[[-1]*n for _ in range(1<<k)]
ans=0
for i in range(k):
    Land[int(input())-1]=i
for i in range(m):
    a,b,c=map(int,input().split())
    D[a-1].append([b-1,c])
    D[b-1].append([a-1,c])
q=deque()
check[0][0]=0
q.append([0,0])
while q:
    key,x=q.popleft()
    if x==0: ans=max(check[key][x],ans)
    if Land[x]!=-1 and not(key & 1<<Land[x]):
        nkey=key | 1<<Land[x]
        if check[nkey][x]<check[key][x]+1:
            check[nkey][x]=check[key][x]+1
            q.append([nkey,x])
    for nx, Max in D[x]:
        if check[key][x]<=Max and check[key][nx]<check[key][x]:
            check[key][nx]=check[key][x]
            q.append([key,nx])
print(ans)