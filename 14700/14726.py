T = int(input())
d = 0
for i in range(T):
    A = str(input())
    a = [0] * len(A)
    for j in range(len(A)):
        if j % 2 == 1:
            a[j] = int(A[j])
        else:
            a[j] = int(A[j])*2
            if a[j] >= 10:
                a[j] = a[j]//10 + a[j]%10
    if sum(a) % 10 == 0:
        print("T")
    else:
        print("F")