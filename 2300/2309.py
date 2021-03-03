A=[];k=0;B=[]
for i in range(9):
    A.append(int(input()))
A.sort()
for i in range(0,8):
    if k==1:break
    for j in range(i+1,9):
        if k==1:break
        if sum(A)-A[i]-A[j]==100:
            B.append(A[i])
            B.append(A[j])
            k=1
for i in range(9):
    if A[i] not in B:print(A[i])