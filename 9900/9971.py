while 1:
    a=input()
    if a=='ENDOFINPUT':break
    k=input()
    ans=''
    for i in range(len(k)):
        if 65<=ord(k[i])<=90:
            c=ord(k[i])-5
            if c<65:c+=26
            ans+=chr(c)
        else:ans+=k[i]
    print(ans)
    input()