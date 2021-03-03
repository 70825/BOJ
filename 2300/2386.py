while 1:
    A = input().split()
    d = 0
    if A[0] == "#":
        break
    for i in range(len(A)):
        A[i] = A[i].lower()
    for i in range(1,len(A)):
        for j in range(len(A[i])):
            if A[0] == A[i][j]:
                d += 1
    print(A[0],d)