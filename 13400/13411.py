from heapq import *
q=[]
for i in range(int(input())):
    a,b,c=map(int,input().split())
    heappush(q,[(a**2+b**2)**.5/c,i+1])
for i in range(len(q)):
    print(heappop(q)[1])