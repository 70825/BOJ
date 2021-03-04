def find(x):
    if(p[x]==x):return x
    p[x] = find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=x
    max_p[y]=0
    now_p[y]=0
input=__import__('sys').stdin.readline
n,l=map(int,input().split())
p=[i for i in range(l)]
max_p=[1]*l
now_p=[0]*l
for i in range(n):
    a,b=map(int,input().split())
    a-=1;b-=1
    if find(p[a])!=find(p[b]):
        max_p[find(p[a])]+=max_p[find(p[b])]
        now_p[find(p[a])]+=now_p[find(p[b])]
        merge(a,b)
    if now_p[find(a)]==max_p[find(a)]:print('SMECE')
    else:now_p[find(a)]+=1;print('LADICA')