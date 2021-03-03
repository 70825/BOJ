def f(x):
    if x==P[x]:return x
    P[x]=f(P[x])
    return P[x]
n=int(input())
input()
P=[i for i in range(n)]
D=[[*map(int,input().split())] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if D[i][j]==1:P[f(i)]=f(j)
S=[*map(int,input().split())]
for i in range(1,len(S)):
    if f(S[0]-1)!=f(S[i]-1):print('NO');exit()
print('YES')