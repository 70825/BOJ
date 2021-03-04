def find(x):
    if(p[x]==x):return x
    p[x] = find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    ans[x]+=ans[y];ans[y]=0
    p[y]=x
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
p=[i for i in range(n)]
path=[[*map(int,input().split())]+[i] for i in range(n)]
min_path=sorted(path,key=lambda a:a[1])
ans=[0]*n
for i in range(n):
    ans[i]=path[i][0]
for i in range(n):
    s,x,t=min_path[i]
    for nt in [t+1,t-1]:
        if 0<=nt<n and x>=path[nt][1]:merge(p[t],p[nt])
    if ans[p[t]] >= m: print(x);break