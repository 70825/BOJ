while 1:
 A=int(input());A=str(A);d=0
 if A=="0":break
 else:
  for i in range(len(A)//2):
   if A[i]==A[len(A)-1-i]:d+=1
  if d==len(A)//2:print("yes")
  else:print("no")