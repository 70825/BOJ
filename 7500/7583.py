while 1:
    S=[*map(str,input().split())]
    if S[0]=='#':break
    for i in range(len(S)):
        if len(S[i])>=4:S[i]=S[i][0]+S[i][1:len(S[i])-1:][::-1]+S[i][len(S[i])-1]
    print(' '.join(S))