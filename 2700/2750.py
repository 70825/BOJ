N = int(input())
A = [0] * N
if 1<= N <= 1000:
    for i in range(N):
        A[i] = int(input())
    A.sort()
    for i in range(N):
        print(A[i])