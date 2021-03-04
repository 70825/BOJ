T=int(input())
D=[];B=[];C=[]
for i in range(T):
    A=str(input())
    D.append(A)
    B.append(A)
    C.append(A)
B.sort()
C.sort(reverse=True)
if D==B:print('INCREASING')
elif D==C:print('DECREASING')
else:print('NEITHER')