from fractions import *
A,B=map(int,input().split(':'))
C=str(Fraction(A,B));k=0
if C.count('/')==0:
    print(C+':1')
else:
    for i in range(len(C)):
        if C[i]!='/':print(C[i],end="")
        else:print(':',end="")