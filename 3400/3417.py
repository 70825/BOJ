while 1:
    b=input()
    if b=='0':break
    a=input()
    c=b*(len(a)//len(b))+b[:len(a)%len(b)]
    d=''
    for i in range(len(a)):
        e=ord(a[i])+ord(c[i])-64*2
        if e>26:e-=26
        d+=chr(e+64)
    print(d)