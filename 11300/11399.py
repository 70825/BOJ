import sys
N = int(input())
S = [0] *N
A = sys.stdin.readline().split()
for i in range(N):
    A[i] = int(A[i])
A.sort()
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1]+A[i]
print(sum(S))