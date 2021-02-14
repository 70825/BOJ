k=1
while 1:
    o,w=map(int,input().split());d=0
    if o==0 and w==0:break
    while 1:
        A,B=map(str,input().split())
        B=int(B)
        if A=='#' and B==0:break
        if A=='F':w+=B
        elif A=='E':w-=B
        if w<=0:d=1
    print(k,end=" ")
    if d==1:print('RIP')
    elif 0.5*o<w<2*o:print(':-)')
    else:print(':-(')
    k+=1