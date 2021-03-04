for i in range(int(input())):
    S=str(input())
    ans=''
    k=''
    for j in range(len(S)):
        if len(k)==0:
            k+=S[j]
        elif k[len(k)-1]==S[j]:
            k+=S[j]
        else:
            ans+=str(len(k))+k[0]
            k=S[j]
    if len(k)!=0:
        ans+=str(len(k))+k[0]
    print(ans)