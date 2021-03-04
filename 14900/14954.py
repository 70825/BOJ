N=int(input());h=0
while N!=1:
    k=0;a=str(N)
    for i in range(len(str(N))):
        k+=int(a[i])**2
    if k==4:h=1;break
    else:N=k
if h==0:print('HAPPY')
else:print('UNHAPPY')