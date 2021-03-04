d=1
while 1:
 A,B,C=input().split();t=0
 if B=="E":break
 else:
  A=int(A);C=int(C)
  if B == ">":
   if A>C:t+=1
  elif B==">=":
   if A>=C:t+=1
  elif B=="<":
   if A<C:t+=1
  elif B=="<=":
   if A<=C:t+=1
  elif B=="==":
   if A==C:t+=1
  elif B=="!=":
   if A!=C:t+=1
  if t==1:print("Case",str(d)+": true")
  else:print("Case",str(d)+": false")
  d+=1