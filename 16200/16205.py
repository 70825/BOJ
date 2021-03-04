A,B=input().split();A=int(A)
def camel(A,B):
 if A==1:print(B)
 elif A==3:
  print(B[0].lower(),end="")
  for i in range(1,len(B)):print(B[i],end="")
  print("")
 else:
  C=[];k=0
  print(B[0],end="")
  for i in range(1,len(B)):
   if B[i-1]=='_':C.append(B[i].upper());k+=1
   else:C.append(B[i])
  for i in range(k):C.remove('_')
  for i in range(len(C)):print(C[i],end="")
  print("")
def snake(A,B):
 if A==2:print(B)
 else:
  print(B[0].lower(),end="")
  for i in range(1,len(B)):
   if B[i]==B[i].upper():print('_'+B[i].lower(),end="")
   else:print(B[i],end="")
  print("")
def pascal(A,B):
 if A==3:print(B)
 elif A==1:
  print(B[0].upper(),end="")
  for i in range(1,len(B)):print(B[i],end="")
  print("")
 else:
  C=[];k=0;print(B[0].upper(),end="")
  for i in range(1,len(B)):
   if B[i-1]=='_':C.append(B[i].upper());k+=1
   else:C.append(B[i])
  for i in range(k):C.remove('_')
  for i in range(len(C)):print(C[i],end="")
  print("")
camel(A,B)
snake(A,B)
pascal(A,B)