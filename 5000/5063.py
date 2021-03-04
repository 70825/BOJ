import sys
N = int(input())
for i in range(N):
    A,B,C = map(int,sys.stdin.readline().split())
    D = B-C
    if A > D:
        print("do not advertise")
    elif A == D:
        print("does not matter")
    else:
        print("advertise")