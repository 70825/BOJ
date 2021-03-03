while 1:
    x=float(input())
    if x==0.0:break
    p=x*5280/4854*1000
    print('{:.2f} English miles equals {:.2f} Roman miles or {:.0f} paces.'.format(x,p*0.001,p))