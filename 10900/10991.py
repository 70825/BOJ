N = int(input())
if N == 1:
    print("*")
else:
    for i in range(N-1):
        for j in range(N+i):
            if N % 2 == 0:
                if j < N-1 -i:
                    print(" ",end="")
                elif i % 2 == 0 and j % 2 == 1:
                    print("*",end="")
                elif i % 2 == 1 and j % 2 == 0:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if j < N - 1 - i:
                    print(" ", end="")
                elif i % 2 == 0 and j % 2 == 0:
                    print("*", end="")
                elif i % 2 == 1 and j % 2 == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("")
    for i in range(2*N-1):
        if i % 2 == 0:
            print("*",end="")
        else:
            print(" ",end="")