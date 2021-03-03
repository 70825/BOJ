while 1:
    A=input().split();d=0
    if A[0]=='-1':break
    for i in range(len(A)-1):
        A[i]=int(A[i])
    for i in range(len(A)-1):
        if A[i]*2 in A:
            d+=1
    print(d)