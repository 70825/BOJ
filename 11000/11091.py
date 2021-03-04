for i in range(int(input())):
    D=[0]*26
    S=str(input()).lower()
    for j in range(len(S)):
        k=ord(S[j])-97
        if 0<=k<=25:D[k]=1
    if min(D)==1:print('pangram')
    else:
        print('missing',end=" ")
        for j in range(26):
            if D[j]==0:print(chr(j+97),end="")
        print("")