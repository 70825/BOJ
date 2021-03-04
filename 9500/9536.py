T=int(input())
for i in range(T):
    D=[]
    A=input().split()
    for j in range(len(A)):
        D.append(A[j])
    while 1:
        B=str(input())
        if B=='what does the fox say?':
            break
        else:
            B=B.split()
            for i in range(D.count(B[2])):
                D.remove(B[2])
    for i in range(len(D)):
        print(D[i],end=" ")
    print("")