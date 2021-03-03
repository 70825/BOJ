def DFS(x,t=0):
    global start,ans
    visit[x]=1
    if t>ans:ans=t;start=x
    for nx,nt in Tree[x]:
        if not visit[nx]:DFS(nx,t+nt)
import sys
sys.setrecursionlimit(20000)
input=__import__('sys').stdin.readline
n=int(input())
Tree=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for i in range(1,n):
    a,b,c=map(int,input().split())
    Tree[a].append([b,c])
    Tree[b].append([a,c])
ans=0;start=0
DFS(1)
visit=[0]*(n+1)
DFS(start,0)
print(ans)