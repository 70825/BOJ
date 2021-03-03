for i in range(int(input())):
    A=input().split()
    if A[1]=='kg':
        A[0]=float(A[0])
        print("{0:.4f}".format(A[0]*2.2046),'lb')
    elif A[1]=='lb':
        A[0]=float(A[0])
        print("{0:.4f}".format(A[0] * 0.4536),'kg')
    elif A[1]=='l':
        A[0]=float(A[0])
        print("{0:.4f}".format(A[0] * 0.2642),'g')
    elif A[1]=='g':
        A[0]=float(A[0])
        print("{0:.4f}".format(A[0]*3.7854),'l')