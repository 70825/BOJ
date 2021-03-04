T=int(input())
for i in range(T):
    A=str(input())
    print('String #'+str(i+1))
    for j in range(len(A)):
        if A[j]=='Z':
            print('A',end="")
        else:
            print(chr(ord(A[j])+1),end="")
    print("")
    print("")