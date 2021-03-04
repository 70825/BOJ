D1,D2=map(int,input().split())
B1,B2=map(int,input().split())
J1,J2=map(int,input().split())
b=0;d=0
while B1!=J1 or B2!=J2:
    if B1>J1:B1-=1;b+=1
    elif B1<J1:B1+=1;b+=1
    elif B2>J2:B2-=1;b+=1
    elif B2<J2:B2+=1;b+=1
while D1!=J1 or D2!=J2:
    if D1>J1 and D2>J2:D1-=1;D2-=1;d+=1
    elif D1>J1 and D2<J2:D1-=1;D2+=1;d+=1
    elif D1<J1 and D2>J2:D1+=1;D2-=1;d+=1
    elif D1<J1 and D2<J2:D1+=1;D2+=1;d+=1
    elif D1<J1:D1+=1;d+=1
    elif D1>J1:D1-=1;d+=1
    elif D2<J2:D2+=1;d+=1
    elif D2>J2:D2-=1;d+=1
if b==d:print('tie')
elif b>d:print('bessie')
else:print('daisy')