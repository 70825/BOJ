while 1:
    A=str(input())
    if A=='.':break
    D=[]
    for i in range(len(A)):
        if A[i]=='(':D.insert(0,A[i])
        elif A[i]=='[':D.insert(0,A[i])
        elif A[i]==')':
            if len(D)==0 or D[0]=='[' or D[0]==']':D.insert(0,A[i])
            elif D[0]=='(':del D[0]
        elif A[i]==']':
            if len(D)==0 or D[0]=='(' or D[0]==')':D.insert(0,A[i])
            elif D[0]=='[':del D[0]
    if len(D)==0:print('yes')
    else:print('no')