T=int(input())
for i in range(T):
 A=str(input());b=0;g=0;B=A.lower()
 for j in range(len(B)):
  if B[j] =='g':g+=1
  elif B[j]=='b':b+=1
 print(A,"is",end=" ")
 if b>g:print("A BADDY")
 elif g>b:print("GOOD")
 else:print("NEUTRAL")