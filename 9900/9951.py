while 1:
    S=str(input()).lower()
    if S=='#':break
    D=[]
    k=''
    for i in range(len(S)):
        if 97<=ord(S[i])<=122 or len(k)!=0 and 48<=ord(S[i])<=57:
            k+=S[i]
        elif k!='' and S[i]==' ':D.append(k);k=''
    if k!='':D.append(k)
    D=sorted(list(set(D)))
    print('\n'.join(D))
    print("")