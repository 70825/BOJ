from collections import deque
for _ in range(int(input())):
    n=int(input())
    D=[-1]*n;D[1%n]=0
    q=deque([1]);ans=0
    while q:
        x=q.popleft()
        if x%n==0:ans=x;break
        for i in [0,1]:
            nx=x*10+i
            if D[nx%n]==-1:
                D[nx%n]=nx;q.append(nx)
    if ans!=0:print(ans)