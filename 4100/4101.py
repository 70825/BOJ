while 1:
    A,B = map(int,input().split())
    if A == B == 0:
        break
    elif A > B:
        print("Yes")
    elif A <= B:
        print("No")