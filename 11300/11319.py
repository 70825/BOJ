T=int(input())
for i in range(T):
    B=['a','e','i','o','u']
    A=str(input())
    A=A.lower();k=0;m=len(A)
    for i in range(len(A)):
        if A[i] in B:
            k+=1
        if A[i] == " ":
            m-=1
    print(m-k,k)