N,K=map(int,input().split())
A=list(map(int,input().split()))
D=[0]*(len(A)-K+1)
for i in range(len(D)):
    for j in range(i,K+i):D[i]+=A[j]
print(max(D))