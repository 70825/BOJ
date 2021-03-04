N = int(input())
A = ["A"] * N
for i in range(N):
    A[i] = str(input())
K = int(input())
if K == 1:
    for i in range(N):
        print(A[i])
elif K == 2:
    for i in range(N):
        for j in range(N-1,-1,-1):
            print(A[i][j],end="")
        print("")
elif K == 3:
    for i in range(N-1,-1,-1):
        print(A[i])