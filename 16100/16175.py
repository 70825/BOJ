for i in range(int(input())):
    A,B=map(int,input().split())
    C=[[0]*A for _ in range(B)];D=[0]*A
    for j in range(B):
        C[j]=input().split()
        C[j]=list(map(int,C[j]))
    for j in range(A):
        for k in range(B):
            D[j]+=C[k][j]
    for j in range(A):
        if max(D)==D[j]:print(j+1)