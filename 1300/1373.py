A=str(input())
A=int(A,2)
A=str(oct(A))
for i in range(2,len(A)):
    print(A[i],end="")