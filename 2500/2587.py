A = [0] * 5
b = 0
for i in range(5):
    K = int(input())
    if K < 100 and K % 10 == 0:
        A[i] = K
B = A
B.sort()

if A[0] > 0 and A[1] > 0 and A[2] > 0 and A[3] > 0 and A[4] > 0:
    print(int(sum(A)/5))
    print(B[2])