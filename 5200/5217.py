T=int(input())
for i in range(T):
    N=int(input())
    print('Pairs for',str(N)+':',end=" ")
    if N==1 or N==2:print("")
    else:
        for j in range((N-1)//2):
            A = j+1
            B = N - A
            if j==(N-1)//2-1:print(A,B)
            else:print(A,B,end=", ")