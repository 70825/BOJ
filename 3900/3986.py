T=int(input());s=0
for i in range(T):
 A=str(input());D=[]
 for j in range(len(A)):
  if len(D)==0:D.insert(0,A[j])
  else:
   if A[j]=='A':
    if D[0]=='A':del D[0]
    else:D.insert(0,A[j])
   elif A[j]=='B':
    if D[0]=='B':del D[0]
    else:D.insert(0,A[j])
 if len(D)==0:s+=1
print(s)