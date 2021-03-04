def Min(D):
    print('Case #' + str(i + 1) + ':', end=" ")
    print(min(D))

for i in range(int(input())):
    A=[*map(int,input().split())]
    N=A[0]
    del A[0]
    A.sort()
    B=sum(A)
    D=[]
    if N==8:
        for a in range(5):
            for b in range(a+1,6):
                for c in range(b+1,7):
                    for d in range(c+1,8):
                        D.append(abs(B-2*(A[a]+A[b]+A[c]+A[d])))
    elif N==6:
        for a in range(4):
            for b in range(a+1,5):
                for c in range(b+1,6):
                    D.append(abs(B-2*(A[a]+A[b]+A[c])))
    elif N==4:
        for a in range(3):
            for b in range(a+1,4):
                D.append(abs(B-2*(A[a]+A[b])))
    else:
        D.append(abs(A[0]-A[1]))
    Min(D)