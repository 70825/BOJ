while 1:
    S=str(input())
    if S=='#':break
    k=''
    for i in range(len(S)):
        if S[i]==' ':k+='%20'
        elif S[i]=='!':k+='%21'
        elif S[i]=='$':k+='%24'
        elif S[i]=='%':k+='%25'
        elif S[i]=='(':k+='%28'
        elif S[i]==')':k+='%29'
        elif S[i]=='*':k+='%2a'
        else:k+=S[i]
    print(k)