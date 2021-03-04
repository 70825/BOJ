for i in range(int(input())):
    S=input().split()
    if len(S[0])!=len(S[1]):
        print(S[0],'&',S[1],'are NOT anagrams.')
    else:
        D=[0]*26;k=0
        for j in range(len(S[0])):
            D[ord(S[0][j])-97]+=1
            D[ord(S[1][j])-97]+=1
        for j in range(26):
            if D[j]%2==1:k+=1
        if k==0:print(S[0],'&',S[1],'are anagrams.')
        else:print(S[0],'&',S[1],'are NOT anagrams.')