while 1:
    D,H,V=map(float,input().split())
    if D==H==V==0:break
    W=16*D/(337**0.5)
    O=9/16*W
    print('Horizontal DPI:',"{0:.2f}".format(H/W))
    print('Vertical DPI:',"{0:.2f}".format(V/O))