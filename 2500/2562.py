A = [0] * 9
C = [0] * 9
for i in range(9):
    B = int(input())
    if 1<= B < 100:
        A[i] = B
        C[i] = A[i]
if min(A) >= 1:
    print(max(A))
    for i in range(9):
        if C[i] == max(A):
            print(i+1)