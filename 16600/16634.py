S=input().split()
if S[0]=='E':
    ans='';k=''
    for j in range(len(S[1])):
        if len(k)==0:k+=S[1][j]
        elif k[len(k)-1]==S[1][j]:k+=S[1][j]
        else:ans+=k[0]+str(len(k));k=S[1][j]
    if len(k)!=0:ans+=k[0]+str(len(k))
    print(ans)
else:
    ans=''
    for j in range(0,len(S[1]),2):
        ans+=S[1][j]*int(S[1][j+1])
    print(ans)