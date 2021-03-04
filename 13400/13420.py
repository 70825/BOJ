for i in range(int(input())):
    A=[*map(str,input().split())]
    A[0]=int(A[0]);A[2]=int(A[2]);A[4]=int(A[4])
    if A[1]=='+':
        if A[0]+A[2]==A[4]:k=1
        else:k=0
    elif A[1]=='-':
        if A[0]-A[2]==A[4]:k=1
        else:k=0
    elif A[1]=='*':
        if A[0]*A[2]==A[4]:k=1
        else:k=0
    else:
        if A[0]//A[2]==A[4]:k=1
        else:k=0
    if k==1:print('correct')
    else:print('wrong answer')