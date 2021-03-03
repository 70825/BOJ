N = int(input())
for i in range(N-1,-1,-1):
    for j in range(2*N-1):
        if N-i-1 <= j <= N+i-1:
            print("*",end="")
        elif j < N-i-1:
            print(" ",end="")
    print("")