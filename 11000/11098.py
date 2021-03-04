T = int(input())
for i in range(T):
    N = int(input())
    A = [0] * N
    B = ["A"] * N
    d = 0
    for j in range(N):
        A[j],B[j] = input().split()
    for j in range(N):
        A[j] = int(A[j])
    for j in range(N):
        if A[j] == max(A):
            d = j
    print(B[d])