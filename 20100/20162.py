N = int(input())
A = [int(input()) for _ in range(N)]
D=[A[i] for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]: D[i] = max(D[i], D[j]+A[i])
print(max(D))