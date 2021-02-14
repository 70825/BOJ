while 1:
    A=str(input())
    if A=='0':break
    k=2+len(A)-1
    for i in range(len(A)):
        if A[i]=='0':k+=4
        elif A[i]=='1':k+=2
        else:k+=3
    print(k)