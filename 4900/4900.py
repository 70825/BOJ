Dict={'063':'0','010':'1','093':'2','079':'3','106':'4','103':'5','119':'6','011':'7','127':'8','107':'9'}
Num={'0':'063','1':'010','2':'093','3':'079','4':'106','5':'103','6':'119','7':'011','8':'127','9':'107'}
while 1:
    S=input()
    if S=='BYE':break
    a,c=S.split('+')
    b=c[:len(c)-1:]
    A,B='',''
    for i in range(0,len(a),3):
        k=a[i]+a[i+1]+a[i+2]
        A+=Dict[k]
    for i in range(0,len(b),3):
        k=b[i]+b[i+1]+b[i+2]
        B+=Dict[k]
    C=str(int(A)+int(B))
    ans=''
    for i in range(len(C)):
        ans+=Num[C[i]]
    print('{}+{}={}'.format(a,b,ans))