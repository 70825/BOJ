A=[];k=0;B=[]
for i in range(9):
    A.append(int(input()))
A.sort()
for i in range(0,8):
    for j in range(i+1,9):
        if sum(A)-A[i]-A[j]==100:
            B.append(A[i])
            B.append(A[j])
for i in range(9):
    if A[i] not in B:print(A[i])