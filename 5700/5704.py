while 1:
 A=str(input());B=[0]*26
 if A=='*':break
 for i in range(len(A)):
  for j in range(26):
   if A[i]==chr(97+j):B[j]+=1
 if min(B)==0:print("N")
 else:print("Y")