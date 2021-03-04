n = int(input())
A = [0] * (n+1)
if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    A[0] = 0
    A[1] = 1
    for i in range(2,n+1):
        A[i] = A[i-1] + A[i-2]
    print(A[n])