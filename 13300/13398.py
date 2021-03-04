N=int(input())
D=[*map(int,input().split())]
L,R=[0]*N,[0]*N
L[0],R[N-1]=D[0],D[N-1]
for i in range(1,N):
    L[i]=max(D[i],L[i-1]+D[i])
for i in range(N-2,-1,-1):
    R[i]=max(D[i],R[i+1]+D[i])
ans=max(L)
for i in range(1,N-1):
    ans=max(ans,L[i-1]+R[i+1])
print(ans)