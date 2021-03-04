while 1:
    C=0;T=0
    A=input().split()
    if A[0]=='#':break
    for i in range(len(A)-1):
        if A[i]=='A' or int(A[i])%2==1:C+=1
        else:T+=1
    if C==T:print('Draw')
    elif C>T:print('Cheryl')
    else:print('Tania')