while 1:
    A,B=map(str,input().split())
    if A=='0' and B=='#':break
    A=int(A)
    C=['January','February','March','April','May','June','July']
    D=['September','October','November','December']
    if B == 'February' and A==29:print('Unlucky')
    elif B in C:print('Yes')
    elif B in D:print('No')
    elif B=='August' and A==4:print('Happy birthday')
    elif B=='August' and A<4:print('Yes')
    else:print('No')