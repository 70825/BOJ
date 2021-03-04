def find(x):
    if(p[x]==x):return x
    p[x] = find(p[x])
    return p[x]
input=__import__('sys').stdin.readline
from collections import deque
n,w=map(int,input().split())
baek,cube=map(int,input().split())
p=[i for i in range(n)]
path=[]
for i in range(w):
    a,b,c=map(int,input().split())
    path.append([a,b,c])
path=sorted(path,key=lambda a:-a[2])
for i in range(w):
    x,y,w=path[i]
    p[find(p[y])]=find(p[x])
    if find(p[baek])==find(p[cube]):print(w);break