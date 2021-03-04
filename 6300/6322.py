k=1
while 1:
    A,B,C=map(int,input().split())
    if A==0 and B==0 and C==0:break
    print('Triangle #'+str(k))
    if C==-1:
        C=(A**2+B**2)**0.5
        print('c =',"{0:.3f}".format(C))
    else:
        if max(A,B)>=C:
            print('Impossible.')
        elif A==-1:
            A=(C**2-B**2)**0.5
            print('a =', "{0:.3f}".format(A))
        elif B==-1:
            B=(C**2-A**2)**0.5
            print('b =', "{0:.3f}".format(B))
    print("")
    k+=1