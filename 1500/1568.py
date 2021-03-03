N=int(input());d=0;k=0
while N>0:
    d+=1
    if N<d:d=1;N-=d;k+=1
    else:N-=d;k+=1
print(k)