while 1:
    S=[*map(str,input().split())]
    if S[0]=='#':break
    for i in range(len(S)):
        for j in range(len(S[i])):
            print(S[i][len(S[i])-1-j],end="")
        print(end=" ")
    print("")