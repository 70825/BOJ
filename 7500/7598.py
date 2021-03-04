while 1:
    A,B=map(str,input().split())
    if A=='#' and B=='0':break
    ans=int(B)
    while 1:
        x,y=map(str,input().split())
        y=int(y)
        if x=='X' and y==0:
            print(A,ans);break
        elif x=='B':
            if ans+y<=68:ans+=y
        else:
            if ans-y>=0:ans-=y