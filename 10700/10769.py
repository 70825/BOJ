A=str(input())
h=0;s=0
if len(A)<=2:print('none')
else:
 for i in range(len(A)-2):
  B=A[i]+A[i+1]+A[i+2]
  if B==':-)':h+=1
  elif B==':-(':s+=1
 if h==0==s:print('none')
 elif h==s:print('unsure')
 elif h>s:print('happy')
 else:print('sad')