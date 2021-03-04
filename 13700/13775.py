N=int(input())%26
S=[*map(str,input().split())]
for i in range(len(S)):
    for j in range(len(S[i])):
        k=ord(S[i][j])-N
        if k<97:k+=26
        if 97<=k<=122:
            print(chr(k),end="")
        else:print(S[i][j],end="")
        N+=1
        if N>25:N-=25
    print(end=" ")