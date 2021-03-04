A=input()
B=input()
C=[]
for i in range(8):
    C.append(int(A[i]))
    C.append(int(B[i]))
while len(C)!=2:
    D=[]
    for i in range(len(C)-1):
        D.append((C[i]+C[i+1])%10)
    C=D
print(str(C[0])+str(C[1]))