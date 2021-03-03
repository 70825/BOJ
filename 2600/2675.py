T = int(input())
for i in range(T):
    A,B = map(str,input().split())
    A = int(A)
    for j in range(len(B)):
        for k in range(A):
            print(B[j],end="")
    print("")