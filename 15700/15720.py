A,B,C=map(int,input().split())
a=sorted([*map(int,input().split())])[::-1]
b=sorted([*map(int,input().split())])[::-1]
c=sorted([*map(int,input().split())])[::-1]
k=min(A,B,C)
ans=sum(a)+sum(b)+sum(c)
total=0
for i in range(k):
    total+=int((a[0]+b[0]+c[0])*0.9)
    a.pop(0);b.pop(0);c.pop(0)
total+=sum(a)+sum(b)+sum(c)
print(ans)
print(total)