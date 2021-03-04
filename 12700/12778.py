for i in range(int(input())):
    M,N=map(str,input().split())
    M=int(M)
    if N=='C':
        A=[*map(str,input().split())]
        for j in range(M):
            print(ord(A[j])-64,end=" ")
    else:
        A=[*map(int,input().split())]
        for j in range(M):
            print(chr(A[j]+64),end=" ")
    print("")