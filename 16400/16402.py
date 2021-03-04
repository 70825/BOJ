def find(x):
    if p[x]==x:return x
    p[x]=find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=x
n,m=map(int,input().split())
p={}
for i in range(n):
    x=input()
    p[x]=x
for i in range(m):
    a,b,c=map(str,input().split(','))
    if find(a)==find(b):
        if c=='1':p[find(b)]=a;p[a]=a
        else:p[find(a)]=b;p[b]=b
    elif c=='1':merge(a,b)
    else:merge(b,a)
ans=0
D=[]
for x in p.keys():
    if p[x]==x:ans+=1;D.append(x)
print(ans)
print('\n'.join(map(str,sorted(D))))