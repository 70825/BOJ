import sys
sys.setrecursionlimit(10**6)
input = __import__('sys').stdin.readline
def find(x):
    if(p[x]==x):return x
    p[x] = find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[x]=y
n = int(input())
m = int(input())
p = list(i for i in range(n))
D = [0]*n
for i in range(m):
    x,y = map(int,input().split())
    x-=1;y-=1
    while x < y:
        x = find(x)
        if x >= y: break
        merge(x, y)
        x += 1
q = list(set(p))
ans=0
for x in q:
    x = find(x)
    if D[x]==0:ans+=1;D[x]=1
print(ans)