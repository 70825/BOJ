N,M=map(int,input().split())
D=[[] for i in range(N+1)]
check=[False]*(N+1)
count=0;p=0
memo=[]
for i in range(M):
    a,b=map(int,input().split())
    D[a].append(b)
    D[b].append(a)
def dfs(k):
    global check,memo
    if check[k]==True:return
    check[k]=True
    memo.append(k)
    for t in D[k]:
        if check[t]==False:dfs(t)
for i in range(1,N+1):
    dfs(i)
    if len(memo) != p:count+=1;p=len(memo)
print(count)