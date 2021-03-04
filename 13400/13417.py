T=int(input())
for i in range(T):
    N=int(input())
    A=input().split()
    D=[A[0]]
    for j in range(1,len(A)):
        if ord(D[0])<ord(A[j]):D.append(A[j])
        else:D.insert(0,A[j])
    for j in range(len(D)):print(D[j],end="")
    print("")