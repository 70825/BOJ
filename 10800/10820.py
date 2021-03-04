while 1:
    try:
        S=str(input());a=0;b=0;c=0;d=0
        for i in range(len(S)):
            if 65<=ord(S[i])<=90:b+=1
            elif 97<=ord(S[i])<=122:a+=1
            elif S[i]==' ':d+=1
            elif 48<=ord(S[i])<=57:c+=1
        print(a,b,c,d)
    except EOFError:break