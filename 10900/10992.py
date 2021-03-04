N = int(input())
if N == 1:
    print("*")
else:
    for i in range(N-1):
        for j in range(2*N-1):
            if j == N-i-1 or j == N+i-1:
                print("*",end="")
            elif j <= N+i-1:
                print(" ",end="")
        print("")
    for i in range(2*N-1):
        print("*",end="")