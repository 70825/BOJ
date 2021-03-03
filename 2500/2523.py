N = int(input())
for i in range(N):
    d = 0
    while d < i+1:
        print("*",end="")
        d += 1
    print("")
for i in range(N-2,-1,-1):
    d = 0
    while d < i+1:
        print("*",end="")
        d += 1
    print("")