N = int(input())
a = [-1] * N
A = input().split()
d = 0
k = 0
for i in range(len(A)):
    A[i] = int(A[i])
for i in range(len(A)):
    if i == 0:
        a[i] = 0
        d = A[i]
        k += 1
    else:
        if a[i-1] != -1 and A[i] > A[i-1]:
            a[i] = A[i] -d
        else:
            d = A[i]
            a[i] = 0
            k += 1
if k == N:
    print("0")
else:
    print(max(a))