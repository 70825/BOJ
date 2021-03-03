while 1:
    A=str(input())
    if A=='0':break
    while len(A)!=1:
        b=0
        for i in range(len(A)):b+=int(A[i])
        A=str(b)
    print(A)