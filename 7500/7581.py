while 1:
    a,b,c,d=map(int,input().split())
    if a==b==c==d==0:break
    if a==0:a=d//(b*c)
    if b==0:b=d//(a*c)
    if c==0:c=d//(a*b)
    if d==0:d=a*b*c
    print(a,b,c,d)