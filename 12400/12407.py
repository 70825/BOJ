for i in range(int(input())):
    A=[*map(int,input().split())]
    del A[0]
    A.sort()
    B=sum(A)
    D=[]
    for a in range(5):
        for b in range(a+1,6):
            for c in range(b+1,7):
                for d in range(c+1,8):
                    D.append(abs(B-2*(A[a]+A[b]+A[c]+A[d])))
    print('Case #'+str(i+1)+':',end=" ")
    print(min(D))