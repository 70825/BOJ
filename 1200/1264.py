while 1:
 A=str(input());d=0;A=A.lower();C=['a','e','i','o','u']
 if A=="#":break
 else:
  for i in range(len(A)):
   if A[i] in C:d+=1
 print(d)