b=0;s=0
for i in range(int(input())):
    a=input().split();c=int(a[1])
    b+=c
    if a[2]=='A+':s+=4.3*c
    elif a[2]=='A0':s+=4*c
    elif a[2]=='A-':s+=3.7*c
    elif a[2]=='B+':s+=3.3*c
    elif a[2]=='B0':s+=3*c
    elif a[2]=='B-':s+=2.7*c
    elif a[2]=='C+':s+=2.3*c
    elif a[2]=='C0':s+=2*c
    elif a[2]=='C-':s+=1.7*c
    elif a[2]=='D+':s+=1.3*c
    elif a[2]=='D0':s+=1*c
    elif a[2]=='D-':s+=0.7*c
c=round(s*100/b,0)
print("{0:.2f}".format(c/100))