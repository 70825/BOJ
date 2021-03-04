from heapq import *
input=__import__('sys').stdin.readline
Pq,Mq=[],[]
for i in range(int(input())):
    n=int(input())
    if n==0:
        if len(Pq)!=0 and (len(Mq)==0 or Pq[0]<Mq[0]):
            print(heappop(Pq))
        elif len(Mq)!=0 and (len(Pq)==0 or Mq[0]<=Pq[0]):
            print(-heappop(Mq))
        else:print(0)
    if n>0:heappush(Pq,n)
    elif n<0:heappush(Mq,-n)