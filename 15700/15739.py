N = int(input())
S = []
a = 0
b = 0
c = 0
d = 0
if 3<= N <= 100:
    A = [[0]*N for i in range(N)]
    for i in range(N):
        B = input()
        C = B.split()
        if len(C) == N:
            A[i] = B.split()
            for j in range(N):
                if 1<=int(A[i][j])<=N**2:
                    A[i][j] = int(A[i][j])
                    a += 1
                    S.append(A[i][j])
        else:
            break
    if a == N ** 2 and len(set(S)) == N ** 2:
        for i in range(N):
            if sum(A[i]) == int(N*(N**2+1)/2):
                c += 1
        for i in range(N):
            for j in range(N):
                b += A[j][i]
            if b == int(N*(N**2+1)/2):
                c += 1
            b = 0
        for i in range(N):
            b += A[i][i]
        if b == int(N*(N**2+1)/2):
            c += 1
        b = 0
        for i in range(N):
            b += A[i][N-1-i]
        if b == int(N*(N**2+1)/2):
            c += 1
    if c == 2*N + 2:
        print("TRUE")
    else:
        print("FALSE")