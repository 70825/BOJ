N,M=map(int,input().split())
a={};b=[]*N
for i in range(N):
    A=str(input());B=int(input());K=[]*B;b.append(A)
    for j in range(B):C=str(input());K.append(C)
    K.sort();a[A]=K
for i in range(M):
    A=str(input());B=int(input())
    if B==1:
        for j in range(N):
            if A in a[b[j]]:print(b[j])
    elif B==0:
        for j in range(len(a[A])):print(a[A][j])