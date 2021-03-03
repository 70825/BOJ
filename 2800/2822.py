A = [0] * 8
B = [0] * 8
for i in range(8):
    A[i] = int(input())
    B[i] = A[i]
B.sort()
C = 0
for i in range(8):
    if A[i] > B[2]:
        C += A[i]
print(C)
for i in range(8):
    if A[i] > B[2]:
        print(i+1,end=" ")