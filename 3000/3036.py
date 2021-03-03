from fractions import Fraction
N=int(input())
A=input().split()
for i in range(N):
    A[i]=int(A[i])
for i in range(1,N):
    B=Fraction(A[0],A[i])
    if B==int(B):
        print(str(B)+'/'+'1')
    else:
        print(B)