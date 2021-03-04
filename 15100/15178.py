for i in range(int(input())):
    A,B,C=map(int,input().split())
    if A+B+C==180:print(A,B,C,'Seems OK')
    else:print(A,B,C,'Check')