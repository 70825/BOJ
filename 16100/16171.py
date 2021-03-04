A=str(input())
B=str(input())
memo=['0','1','2','3','4','5','6','7','8','9']
C=''
for i in range(len(A)):
    if A[i] not in memo:C+=A[i]
if B in C:print(1)
else:print(0)