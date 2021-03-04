def find(x):
    if p[x]==x: return x
    p[x] = find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    if x==y:return False
    p[y]=x
    return True
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[]
for i in range(m+1):
    D.append([*map(int,input().split())])
worst=sorted(D,key=lambda a:a[2])
best=sorted(D,key=lambda a:-a[2])
W,B=0,0
rW,rB=0,0
p=[i for i in range(n+1)]
for i in range(len(worst)):
    x,y,z=worst[i]
    if merge(x,y):
        if z==0:W+=1
        rW+=1
        if rW==n:break
p=[i for i in range(n+1)]
for i in range(len(best)):
    x,y,z=best[i]
    if merge(x,y):
        if z==0:B+=1
        rB+=1
        if rB==n:break
print(W**2-B**2)