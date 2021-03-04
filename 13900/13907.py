input=__import__('sys').stdin.readline
Max=float('inf')
n,m,k=map(int,input().split())
s,e=map(int,input().split())
D=[[] for _ in range(n+1)]
for i in range(m):
    a,b,w=map(int,input().split())
    D[a].append((b,w))
    D[b].append((a,w))
S=[[Max]*(n+1) for _ in range(n+1)];S[s][0]=0
for y in range(n):
    for x in range(1,n+1):
        if S[x][y]==Max:continue
        for nx,nt in D[x]:
            S[nx][y+1]=min(S[nx][y+1],S[x][y]+nt)
print(min(S[e]))
for i in range(k):
    z=int(input())
    for j in range(n+1):S[e][j]+=j*z
    print(min(S[e]))