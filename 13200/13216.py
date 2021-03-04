S=input()
A,B,a,b=0,0,0,0
for i in range(len(S)):
    if S[i]=='A':a+=1
    else:b+=1
    if a==21 or b==21 or i==len(S)-1:
        print(str(a)+'-'+str(b))
        if a==21:A+=1
        else:B+=1
        a=0;b=0
if A>B:print('A')
else:print('B')