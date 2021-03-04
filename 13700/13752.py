N = int(input())
K = "="
if 1<= N <=100:
    A = [0] * N
    for i in range(N):
        B = int(input())
        if 1<= B<=80:
            A[i] = B
    if min(A) > 0:
        for i in range(N):
            for j in range(A[i]):
                print("=",end="")
                if j == A[i] - 1:
                    print("")