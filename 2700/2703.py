for i in range(int(input())):
    S=input();k=input()
    for j in range(len(S)):
        if 0<=ord(S[j])-65<=25:print((k[ord(S[j])-65]),end="")
        else:print(S[j],end="")
    print("")