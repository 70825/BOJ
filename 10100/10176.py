for i in range(int(input())):
    S=str(input()).lower()
    ans=0
    for j in range(len(S)):
        if 97<=ord(S[j])<=122:
            ans+=ord(S[j])-96
    if ans%27==0:print('Yes')
    else:print('No')