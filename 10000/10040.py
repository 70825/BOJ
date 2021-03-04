N,M=map(int,input().split())
A=[0]*N;B=[0]*N
for i in range(N):
    A[i]=int(input())
for i in range(M):
    C=int(input())
    for j in range(N):
        if A[j]<=C:B[j]+=1;break
for i in range(N):
    if max(B)==B[i]:k=i+1
print(k)