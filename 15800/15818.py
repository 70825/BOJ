N, M =input().split()
N = int(N)
M = int(M)
C = [0] * N
a = 1
if 1<=N<=100 and 1<=M<=2147483647:
    A = input()
    B = A.split()
    for i in range(N):
        if 1<=int(B[i])<=2147483647:
            B[i] = int(B[i])
            a *= B[i]
    print(a % M)