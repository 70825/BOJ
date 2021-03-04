A=int(input())
D=['sukhwan','baby','sukhwan','tururu','turu','very','cute','tururu','turu','in','bed','tururu','turu','baby']
E=[0,1,2,5,6,9,10,13];F=[3,7,11];G=[4,8,12];a='tururu';b='turu'
if A%14 in E:print(D[A%14])
else:
    if A//14<=2:
        if A%14 in F:
            for i in range(A//14):a+='ru'
            print(a)
        elif A%14 in G:
            for i in range(A//14):b+='ru'
            print(b)
    elif A//14==3:
        if A%14 in F:print('tu+ru*'+str(2+A//14))
        else:print('tururururu')
    else:
        if A%14 in F:print('tu+ru*'+str(2+A//14))
        else:print('tu+ru*'+str(1+A//14))