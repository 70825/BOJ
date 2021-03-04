import sys
while 1:
    A,B,C = map(int,sys.stdin.readline().split())
    if A == B == C == 0:
        break
    elif max(A,B,C) >= (A+B+C) - max(A,B,C):
        print("Invalid")
    else:
        if A == B == C:
            print("Equilateral")
        elif A == B or B == C or C == A:
            print("Isosceles")
        else:
            print("Scalene")