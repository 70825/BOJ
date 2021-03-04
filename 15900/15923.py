T=int(input());k=0
C=[];D=[]
A,B=map(int,input().split())
C.insert(0,A);D.insert(0,B)
for i in range(1,T):
    A,B=map(int,input().split())
    if C[0]==A:k+=abs(B-D[0])
    else:k+=abs(A-C[0])
    C.insert(0,A);D.insert(0,B)
if C[0]==C[len(C)-1]:k+=abs(D[0]-D[len(D)-1])
else:k+=abs(C[0]-C[len(C)-1])
print(k)