while 1:
    a=input().split();D=[];s=''
    if a[0]=='#':break
    for i in range(len(a[0])):
        k=ord(a[1][i])-ord(a[0][i])
        b=ord(a[2][i])
        if k+b>122:s+=chr(k+b-26)
        elif k+b<97:s+=chr(k+b+26)
        else:s+=chr(k+b)
    print(' '.join(map(str,a))+' '+s)