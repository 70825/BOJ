N,K=map(int,input().split())
A=[*map(int,input().split())]
k=0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i]+A[j]==K:
            k+=1
print(k)