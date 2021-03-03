n = int(input())
A = [0] * (n+1)
A[1] = 1
if n == 1:
    print(A[n])
elif 2 <= n <= 90:
    A[0] = 0
    A[1] = 1
    for i in range(2,n+1,1):
        A[i] = A[i-1] + A[i-2]
    print(A[n])