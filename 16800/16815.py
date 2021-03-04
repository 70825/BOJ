x=0;y=0;k=input()
for i in range(len(k)):
    if k[i]=='*':a=i;break
for i in range(a+1,len(k)):
    if k[i]=='(':x+=1
    else:y+=1
print(y-x)