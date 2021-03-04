N = int(input())
B = input()
A = B.split()
k= 0
for i in range(5):
    A[i] = int(A[i])
    if A[i] == N:
        k += 1
print(k)