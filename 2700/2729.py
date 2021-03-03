for i in range(int(input())):
    A,B=map(str,input().split())
    A=int(A,2);B=int(B,2)
    C=bin(A+B)
    for j in range(2,len(C)):
        print(C[j],end="")
    print("")