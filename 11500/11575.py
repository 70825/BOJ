T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    C=str(input());D=[]
    for j in range(len(C)):
        D.append(chr(((A*(ord(C[j])-65)+B)%26)+65))
    for j in range(len(D)):
        print(D[j],end="")
    print("")