N,M=map(int,input().split())
A=input().split()
for i in range(N):
    A[i]=int(A[i])
B=input().split()
for i in range(M):
    B[i]=int(B[i])
print(max(A)+max(B))