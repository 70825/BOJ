N = int(input())
for i in range(N):
    for j in range(2*N):
        if i >= j or 2*N-1-i <= j:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
for i in range(N-2,-1,-1):
    for j in range(2*N):
        if i >= j or 2 * N - 1 - i <= j:
            print("*", end="")
        else:
            print(" ", end="")
    print("")