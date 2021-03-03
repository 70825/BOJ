while 1:
    a,b=map(float,input().split())
    if a==b==0:break
    print('{0:.3f}'.format((1-b**2/a**2)**.5))