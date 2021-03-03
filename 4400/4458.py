T=int(input())
for i in range(T):
 A=str(input())
 for j in range(len(A)):
  if j==0:print(A[0].upper(),end="")
  else:print(A[j],end="")
 print("")