A,B = map(int,input().split())
N = [[0] * B for i in range(A)]
for i in range(A):
    C = input().split()
    for j in range(B):
        N[i][j] = int(C[j])
Q,W = map(int,input().split())
M = [[0] * W for i in range(Q)]
for i in range(Q):
    D = input().split()
    for j in range(W):
        M[i][j] = int(D[j])
L = [[0]*W for i in range(A)]
for i in range(B):
    for j in range(A):
        for k in range(W):
            L[j][k] += N[j][i]*M[i][k]
for i in range(A):
    for j in range(W):
        print(L[i][j],end=" ")
    print("")