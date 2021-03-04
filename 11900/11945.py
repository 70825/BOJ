N,M = map(int,input().split())
A = [0] * N
for i in range(N):
    A[i] = str(input())
for i in range(N):
    for j in range(M):
        print(A[i][M-1-j],end="")
    print("")