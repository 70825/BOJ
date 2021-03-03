def find(x):
    if(p[x]==x):return x
    p[x] = find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=x
for __ in range(int(input())):
    p={}
    Set={}
    for _ in range(int(input())):
        a,b=map(str,input().split())
        if a not in p:p[a]=a;Set[a]=1
        if b not in p:p[b]=b;Set[b]=1
        if find(p[a])!=find(p[b]):
            Set[find(p[a])] += Set[find(p[b])]
        merge(a,b)
        print((Set[find(a)]))