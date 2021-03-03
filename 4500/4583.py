while 1:
    S=str(input())[::-1]
    if S=='#':break
    memo=['i','o','v','w','x']
    ans=''
    k=0
    for i in range(len(S)):
        if S[i]=='d':ans+='b'
        elif S[i]=='b':ans+='d'
        elif S[i]=='p':ans+='q'
        elif S[i]=='q':ans+='p'
        elif S[i] in memo:ans+=S[i]
        else:k+=1
    if k==0:print(ans)
    else:print('INVALID')