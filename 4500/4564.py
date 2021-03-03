while 1:
    A=str(input())
    if A=='0':break
    print(A,end=" ")
    while len(A)!=1:
        k=1
        for i in range(len(A)):k*=int(A[i])
        print(k,end=" ");A=str(k)
    print("")