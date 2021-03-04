from collections import deque
A,B=map(int,input().split())
q=deque([(A,1)])
while q:
    x,t=q.popleft()
    if x==B:print(t);exit()
    if x*2<=B:q.append((x*2,t+1))
    k=int(str(x)+'1')
    if k<=B:q.append((k,t+1))
print(-1)