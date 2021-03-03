N=int(input());k=0
while 1:
    if k*(k+1)//2>N:print(k-1);break
    elif k*(k+1)//2==N:print(k);break
    else:k+=1