from collections import deque
D=['0','1','2']
n=int(input())
q=deque(['1','2'])
ans=0
while q:
    x=q.popleft()
    if len(x)==n and int(x)%3==0:ans+=1
    for i in range(3):
        nx=x+D[i]
        if len(nx)<=n:q.append(nx)
print(ans)