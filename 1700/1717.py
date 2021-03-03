def find(t):
    if(p[t]==t):return t
    p[t] = find(p[t])
    return p[t]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=x
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
p=[i for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:merge(b,c)
    else:
        if find(b)==find(c):print('YES')
        else:print('NO')