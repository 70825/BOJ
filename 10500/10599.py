while 1:
    A,B,C,D = map(int,input().split())
    if A == B == C == D == 0:
        break
    print(abs(B-C),abs(A-D))