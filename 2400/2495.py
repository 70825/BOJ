for i in range(3):
    S=str(input())
    k=1;s=1
    for j in range(1,len(S)):
        if S[j]==S[j-1]:s+=1
        else:s=1
        if s>k:k=s
    print(k)