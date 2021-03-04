while 1:
    D=input()
    if D=='#':break
    A,B,a,b=0,0,0,0
    for i in range(len(D)):
        if D[i]=='A':a+=1
        else:b+=1
        if max(a,b)-min(a,b)>=2 and max(a,b)>=4:
            if a>b:A+=1
            else:B+=1
            a=0;b=0
    print('A {} B {}'.format(A,B))