for i in range(int(input())):
    S=str(input())
    a=int(len(S)**0.5)
    for j in range(a):
        for k in range(0,len(S),a):
            print(S[k+a-1-j],end="")
    print("")