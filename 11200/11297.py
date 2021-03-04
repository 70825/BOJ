while 1:
    a,b,c=map(int,input().split())
    if a==b==c==0:break
    k=(a+b+c)%25+1
    S=input()
    for i in range(len(S)):
        if 97<=ord(S[i])<=122:
            if ord(S[i])-k<97:
                print(chr(ord(S[i])-k+26),end="")
            else:print(chr(ord(S[i])-k),end="")
        else:print(S[i],end="")
    print("")