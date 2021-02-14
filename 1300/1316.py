T=int(input());s=0
for i in range(T):
    A=str(input());r=1
    D=[];D.append(A[0])
    for j in range(1,len(A)):
        k=D.count(A[j])
        if k==0:D.append(A[j])
        else:
            if A[j-1]==A[j]:D.append(A[j])
            else:r=0
    if r==1:s+=1
print(s)