for i in range(int(input())):
    A,B=map(int,input().split())
    C=(B-A)**0.5;c=int(C)
    if C==0:print(0)
    elif C==c:print(c*2-1)
    elif (B-A)-c**2>c:print(c*2+1)
    else:print(c*2)