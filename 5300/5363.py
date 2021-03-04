T=int(input())
for i in range(T):
 A=input().split()
 for j in range(2,len(A)):print(A[j],end=" ")
 print(A[0],A[1])