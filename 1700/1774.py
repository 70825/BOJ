def find(x):
    if x==p[x]:return x
    p[x]=find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=p[x]
def Len(x1,y1,x2,y2):return ((x2-x1)**2+(y2-y1)**2)**0.5
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
p=[i for i in range(n)]
God=[[*map(int,input().split())] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    merge(a-1,b-1)
D=[]
for i in range(n):
    x1,y1=God[i]
    for j in range(i+1,n):
        x2,y2=God[j]
        D+=[[Len(x1,y1,x2,y2),i,j]]
D=sorted(D)
ans=0
for i in range(len(D)):
    a,b,c=D[i]
    if find(b)!=find(c):
        ans+=a
        merge(b,c)
print(format(ans,".2f"))