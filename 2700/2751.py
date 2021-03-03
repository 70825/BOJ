N = int(input())
B = [0] * N
if 1<=N<=1000000:
    for i in range(N):
        A = int(input())
        if A <= abs(1000000):
            B[i] = A
        else:
            break
    B.sort()
    for i in range(N):
        print(B[i])