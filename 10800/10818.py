N = int(input())
B = input()
A = B.split()
for i in range(N):
    A[i] = int(A[i])
print(min(A),max(A))