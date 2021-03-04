for i in range(int(input())):
    C=int(input())
    N=int(input())
    A=[*map(int,input().split())]
    print('Case #'+str(i+1)+':',end=" ")
    for j in range(N-1):
        for k in range(j+1,N):
            if A[j]+A[k]==C:
                print(j+1,k+1)