A = input()
K,N,M = A.split()
K = int(K)
N = int(N)
M = int(M)
if 1<=K<=1000 and 1<=N<=1000 and 1<=M<=100000:
    J = K * N
    if M >= J:
        print("0")
    else:
        print(J-M)