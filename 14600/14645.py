A = input()
N,K = A.split()
N = int(N)
K = int(K)
if 1<=N<=100000:
    for i in range(N):
        B = input()
        X, Y = B.split()
        X = int(X)
        Y = int(Y)
        if 0<=X<=10000 and 0<=Y<=10000:
            K += X
            K -= Y
            if K > 10000:
                break
    print("비와이")