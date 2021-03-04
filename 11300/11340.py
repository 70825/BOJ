for i in range(int(input())):
    a,b,c=map(int,input().split())
    for j in range(100):
        d=j+1
        avg=a*15+20*b+25*c+40*d
        if avg/100>=90:print(d);break
        elif d==100:print('impossible');break