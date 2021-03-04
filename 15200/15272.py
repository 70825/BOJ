S=input();k=0
for i in range(1,len(S)):
    if S[i-1]+S[i]=='ss':k=1
if k==1:print('hiss')
else:print('no hiss')