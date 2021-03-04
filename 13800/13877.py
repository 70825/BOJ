for i in range(int(input())):
    A,B=map(int,input().split())
    B=str(B)
    print(A,end=" ")
    try:print(int(B,8),end=" ")
    except ValueError:print(0,end=" ")
    print(B,end=" ")
    try:print(int(B,16))
    except ValueError:print(0)