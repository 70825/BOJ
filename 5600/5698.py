while True:
    A=[*map(str,input().split())]
    if A[0]=='*':break
    for i in range(len(A)):
        A[i]=A[i][0].lower()
    if len(set(A))==1:print('Y')
    else:print('N')