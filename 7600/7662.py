from collections import defaultdict
from heapq import *
input = __import__('sys').stdin.readline
for _ in range(int(input())):
    k = int(input())
    min_q = []
    max_q = []
    d = defaultdict(lambda:0)
    for i in range(k):
        a,b= input().split();b=int(b)
        if a == 'I':
            heappush(min_q,b)
            heappush(max_q,-b)
            d[b] += 1
        if a == 'D':
            if b == 1:
                while max_q:
                    x = -heappop(max_q)
                    if d[x] > 0: d[x]-=1;break
            else:
                while min_q:
                    x = heappop(min_q)
                    if d[x] > 0:d[x] -=1;break
    while len(max_q):
        if d[-max_q[0]]:break
        heappop(max_q)
    while len(min_q):
        if d[min_q[0]]:break
        heappop(min_q)
    if len(min_q):print(-max_q[0],min_q[0])
    else:print('EMPTY')