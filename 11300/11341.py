D=['a','e','i','o','u','y']
for i in range(int(input())):
    S=[*map(str,input().split())]
    for j in range(len(S)):
        for k in range(len(S[j])):
            if S[j][0] in D and k==0:
                S[j]+='yay';break
            elif S[j][0] in D:
                S[j]+='ay';break
            else:
                S[j]+=S[j][0]
                S[j]=S[j][1::]
        if len(S[j])<2 or S[j][len(S[j])-2::]!='ay':
            S[j]+='ay'
        print(S[j],end=" ")
    print("")