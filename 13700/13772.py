for i in range(int(input())):
    A=str(input());k=0
    D=['A','D','O','P','Q','R']
    for j in range(len(A)):
        if A[j] in D:k+=1
        elif A[j]=='B':k+=2
    print(k)