def PRINT(ans,z):
    if ans==0:print('Case {}: No trees.'.format(z))
    elif ans == 1:print('Case {}: There is one tree.'.format(z))
    else:print('Case {}: A forest of {} trees.'.format(z, ans))
def A(x):
    cnt = 1
    check[x]=1
    for nx in Tree[x]:
        if not check[nx]:
            cnt += A(nx)
    return cnt
def B(x):
    cnt = len(Tree[x])
    Pass[x]=1
    for nx in Tree[x]:
        if not Pass[nx]:
            cnt += B(nx)
    return cnt
from collections import deque
input=__import__('sys').stdin.readline
z=1
while z:
    n,m=map(int,input().split())
    if n==m==0:break
    check=[0]*n
    Pass=[0]*n
    Tree=[[] for _ in range(n)]
    ans=0
    for i in range(m):
        a,b=map(int,input().split())
        Tree[a-1].append(b-1)
        Tree[b-1].append(a-1)
    for i in range(n):
        if not check[i]:
            V,E=A(i),B(i)
            if V-1==E//2:ans+=1
    PRINT(ans,z)
    z+=1