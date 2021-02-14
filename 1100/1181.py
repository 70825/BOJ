N = int(input())
A = ["a"] * N
B = []
for i in range(N):
    A[i] = str(input())
B = list(set(A))
B.sort()
B.sort(key=len)
for i in range(len(B)):
    print(B[i])