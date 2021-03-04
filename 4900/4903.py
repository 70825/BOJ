while 1:
    a,b=map(int,input().split())
    if a == b == -1: break
    if a==1 or b==1:print('{}+{}={}'.format(a,b,a+b))
    else:print('{}+{}!={}'.format(a,b,a+b))