from heapq import *
n=int(input())
q=[]
for i in range(n):
    D=[*map(int,input().split())]
    for j in range(n):
        heappush(q,D[j])
        if len(q)==n+1:heappop(q)
print(heappop(q))