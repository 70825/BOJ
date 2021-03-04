from math import *
for _ in range(int(input())):
    if _!=0:print()
    A=input().split()
    print('Equation',_+1)
    if int(A[0][:len(A[0])-1:])==0:
        if int(A[4])-int(A[2])!=0:print('No solution.');continue
        else:print('More than one solution.');continue
    a=(trunc((int(A[4])-int(A[2]))/int(A[0][:len(A[0])-1:])*10**6))
    k=str(abs(a))
    if len(k)<=6:
        if a<0:print('x = {}'.format('-0.'+'0'*(6-len(k))+k))
        else: print('x = {}'.format('0.'+'0'*(6-len(k))+k))
    else:
        if a<0:print('x = -{}'.format(k[:len(k)-6:]+'.'+k[len(k)-6:]))
        else:print('x = {}'.format(k[:len(k)-6:]+'.'+k[len(k)-6:]))