import math
A = input()
B = A.split()
if len(B) == 3:
    N,W,H = A.split()
    N = int(N)
    W = int(W)
    H = int(H)
    if 1<=N<=50 and 1<=W<=100 and 1<=H<=100:
        for i in range(N):
            D = int(input())
            if 1<=D<=1000:
                if D<=math.sqrt(W**2+H**2):
                    print("DA")
                else:
                    print("NE")