A=str(input())
B=int(A,2)*17
B=str(bin(B))
for i in range(2,len(B)):
    print(B[i],end="")