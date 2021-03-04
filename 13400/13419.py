T=int(input())
for i in range(T):
    A=str(input())
    if len(A)%2==0:
        for j in range(len(A)//2):print(A[2*j],end="")
        print("")
        for j in range(len(A)//2):print(A[2*j+1],end="")
    else:
        S=A+A
        for j in range(len(A)):print(S[2*j],end="")
        print("")
        for j in range(len(A)):print(S[2*j+1],end="")
    print("")