while 1:
    A,B,C = input().split()
    A=int(A);C=int(C)
    if A==0 and B=='W' and C==0:
        break
    if B=='W':
        if A-C<-200:
            print("Not allowed")
        else:
            print(A-C)
    else:
        print(A+C)