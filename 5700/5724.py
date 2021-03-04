while 1:
    N=int(input());k=0
    if N==0:break
    while N!=0:k+=N**2;N-=1
    print(k)