a=input()
b=input()
c=b*(len(a)//len(b))+b[:len(a)%len(b)]
d=''
for i in range(len(a)):
    if 97<=ord(a[i])<=122:
        e=ord(a[i])-ord(c[i])
        if e<=0:e+=26
        d+=chr(e+96)
    else:d+=a[i]
print(d)