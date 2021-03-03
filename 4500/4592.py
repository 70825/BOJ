while 1:
 A=input().split()
 if A[0]=='0':break
 D=[];k=1;D.append(int(A[1]))
 for i in range(1,len(A)):
  if D[k-1]!=int(A[i]):D.insert(k,int(A[i]));k+=1
 for i in range(len(D)):print(D[i],end=" ")
 print("$")