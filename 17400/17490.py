def find(x):
    if x==p[x]:return x
    p[x]=find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=p[x]
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
S=[*map(int,input().split())]
for i in range(n):
    S[i]=[S[i],i+1]
p=[i for i in range(n+1)]
go=[1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    if (a==n and b==1) or (a==1 and b==n):go[1]=0
    else:go[max(a,b)]=0
if go[1]==1:merge(1,n)
for i in range(2,n+1):
    if go[i]==1:merge(i-1,i)
if max(p[1::])==1:print('YES');sys.exit(0)
res=0
S=sorted(S)
for i in range(n):
    if find(0)!=find(S[i][1]):
        res+=S[i][0]
        merge(0,S[i][1])
print(['YES','NO'][res>k])