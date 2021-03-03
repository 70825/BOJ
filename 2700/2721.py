T = int(input())
for i in range(T):
    N = int(input())
    W = 0
    for j in range(1,N+1):
        W += (j*(j+1)*(j+2))//2
    print(W)