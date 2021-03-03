def find(x):
    if x==p[x]:return x
    p[x]=find(p[x])
    return p[x]
def merge(x,y):
    x=find(x);y=find(y)
    p[y]=p[x]
def Length(x1,y1,x2,y2): return ((x2-x1)**2+(y2-y1)**2)**0.5
n=int(input())
star=[]
p=[i for i in range(n)]
for i in range(n):
    star.append([*map(float,input().split())])
D=[]
for i in range(n):
    x,y=star[i]
    for j in range(i,n):
        nx,ny=star[j]
        if i!=j:D.append([Length(x,y,nx,ny),i,j])
D=sorted(D)
ans=0
for i in range(len(D)):
    if find(D[i][1])!=find(D[i][2]):
        ans+=D[i][0]
        merge(D[i][1],D[i][2])
print(ans)