from math import log
for i in range(int(input())):
    A=input().split('=')
    if A[0]=='H ':
        print("{0:.2f}".format(-log(float(A[1]),10)))
    else:
        print("{0:.2f}".format(14+log(float(A[1]),10)))