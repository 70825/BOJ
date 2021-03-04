N=int(input())
A=[*map(int,input().split())]
D=[1]*N;S=[-1]*N
for i in range(N):
    for j in range(i):
        if A[i]>A[j] and D[j]+1>D[i]:D[i]=D[j]+1;S[i]=j
ans=max(D);print(ans)
t=[i for i,x in enumerate(D) if x==ans][0]
def go(t):
    if t==-1:return
    go(S[t])
    print(A[t],end=' ')
go(t)