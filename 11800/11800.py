for i in range(int(input())):
 a=[0]*2;a[0],a[1]=map(int,input().split());b=['Yakk','Doh','Seh','Ghar','Bang','Sheesh'];c=['Habb Yakk','Dobara','Dousa','Dorgy','Dabash','Dosh'];print('Case',str(i+1)+':',end=" ")
 if a[0]==a[1]:print(c[a[0]-1])
 else:
  x,y=max(a),min(a)
  if x==6 and y==5:print('Sheesh Beesh')
  else:print(b[x-1],b[y-1])