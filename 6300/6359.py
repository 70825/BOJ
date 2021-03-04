for i in range(int(input())):
    N=int(input())
    D=[1]*(N+1)
    for j in range(2,N+1):
        k=j
        while k<=N:
            if D[k]==0:D[k]=1;
            else:D[k]=0
            k+=j
    print(D.count(1)-1)