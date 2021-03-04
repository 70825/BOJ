while 1:
    A,B,C=map(int,input().split())
    if A==B==C==0:break
    if A==0:print(C//B,B,C)
    elif B==0:print(A,C//A,C)
    else:print(A,B,A*B)