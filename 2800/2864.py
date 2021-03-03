A,B=map(str,input().split())
def mx(k):
    D=[];p=''
    for i in range(len(k)):
        D.append(k[i])
        if D[i]=='5':D[i]='6'
    for i in range(len(k)):p+=D[i]
    return p
def mn(k):
    D=[];p=''
    for i in range(len(k)):
        D.append(k[i])
        if D[i]=='6':D[i]='5'
    for i in range(len(k)):p+=D[i]
    return p
print(int(mn(A))+int(mn(B)),int(mx(A))+int(mx(B)))