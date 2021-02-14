def DFS(x,t=0):
    global start,ans
    visit[x]=1
    if t>ans:ans=t;start=x
    for nx,nt in Tree[x]:
        if not visit[nx]:DFS(nx,t+nt)
import sys
sys.setrecursionlimit(100000)
input=__import__('sys').stdin.readline
n=int(input())
Tree=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for i in range(n):
    D=[*map(int,input().split())]
    for j in range(1,len(D)-1,2):
        a,b,c=D[0],D[j],D[j+1]
        Tree[a].append([b,c])
        Tree[b].append([a,c])
ans=0;start=0
DFS(1)
visit=[0]*(n+1)
DFS(start,0)
print(ans)