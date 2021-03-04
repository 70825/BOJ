T=int(input())
for i in range(T):
 A=input().split();d=0
 for j in range(0,5,2):A[j]=int(A[j])
 if A[1]=='+':
  if A[0]+A[2]==A[4]:d+=1
 elif A[1]=='-':
  if A[0]-A[2]==A[4]:d+=1
 print('Case',str(i+1)+':',end=" ")
 if d==1:print('YES')
 else:print('NO')