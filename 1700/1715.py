from heapq import *
input=__import__('sys').stdin.readline
n=int(input())
q=[]
ans=0
for i in range(n):
    heappush(q,int(input()))
while len(q)!=1:
    x=heappop(q)
    y=heappop(q)
    ans+=x+y
    heappush(q,x+y)
print(ans)