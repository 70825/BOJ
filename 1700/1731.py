N = int(input())
A = [0] * N
d = 0
for i in range(N):
    A[i] = int(input())
if A[1] - A[0] == A[2] - A[1]:
    print(A[N-1]+A[1]-A[0])
else:
    print(int(A[N-1]*(A[1]/A[0])))