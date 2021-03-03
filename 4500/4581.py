while 1:
    S=str(input())
    if S=='#':break
    yes=0
    no=0
    Not=0
    Abs=0
    for i in range(len(S)):
        if S[i]=='Y':yes+=1
        elif S[i]=='N':no+=1
        elif S[i]=='P':Not+=1
        else:Abs+=1
    if len(S)<=Abs*2:print('need quorum')
    elif yes>no:print('yes')
    elif no>yes:print('no')
    else:print('tie')