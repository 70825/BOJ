N = str(input())
A = [0] * len(N)
for i in range(len(N)):
    A[i] = N[i]
A.sort(reverse=True)
for i in range(len(A)):
    print(A[i],end="")