for i in range(int(input())):
    A=input().split()
    print('Distances:',end=" ")
    for j in range(len(A[0])):
        if ord(A[1][j])-ord(A[0][j])<0:
            print(ord(A[1][j])-ord(A[0][j])+26,end=" ")
        else:
            print(ord(A[1][j])-ord(A[0][j]),end=" ")
    print("")