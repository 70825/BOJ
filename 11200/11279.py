from heapq import *
input=__import__('sys').stdin.readline
n=int(input())
q=[]
for i in range(n):
    k=int(input())
    if k==0:
        if len(q)==0:print(0)
        else:print(-int(heappop(q)))
    else:heappush(q,-k)