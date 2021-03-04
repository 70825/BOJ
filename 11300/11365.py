while 1:
    A = str(input())
    if A=="END":
        break
    else:
        for i in range(len(A)-1,-1,-1):
            print(A[i],end="")
        print("")