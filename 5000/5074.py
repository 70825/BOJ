while 1:
    a,b=map(str,input().split())
    if a==b=='00:00':break
    a_h,a_m=map(int,a.split(':'))
    b_h,b_m=map(int,b.split(':'))
    k=a_h*60+b_h*60+a_m+b_m
    x=k//(60*24)
    k-=x*60*24
    y=k//60
    k-=y*60
    print('{:02d}:{:02d} '.format(y,k),end='')
    if x!=0:print('+'+str(x))
    else:print()