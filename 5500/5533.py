N = int(input())
A = [0] * (N+1)
B = [0] * (N+1)
C = [0] * (N+1)
D = [0] * (N+1)
for i in range(1,N+1):
    A[i],B[i],C[i] = map(int,input().split())
for i in range(1,N+1):
    if A.count(A[i]) == 1:
        D[i] += A[i]
    if B.count(B[i]) == 1:
        D[i] += B[i]
    if C.count(C[i]) == 1:
        D[i] += C[i]
for i in range(1,N+1):
    print(D[i])