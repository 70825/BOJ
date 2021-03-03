while 1:
    N=input();D=[]
    if N=='#':break
    for i in range(len(N)):D.append(N[i])
    if N[len(N)-1]=='e':
        if N.count('1')%2==0:D[len(D)-1]='0'
        else:D[len(D)-1]='1'
    else:
        if N.count('1')%2==0:D[len(D)-1]='1'
        else:D[len(D)-1]='0'
    for i in range(len(D)):print(D[i],end="")
    print("")