for _ in range(int(input())):
    a,b=map(str,input().split())
    D={}
    for i in range(len(a)):
        if a[i] not in D:D[a[i]]=1
        else:D[a[i]]+=1
    err=0
    for i in range(len(b)):
        if b[i] not in D or D[b[i]]<=0:err+=1
        else:D[b[i]]-=1
    if err>0 or len(a)!=len(b):print('Impossible')
    else:print('Possible')