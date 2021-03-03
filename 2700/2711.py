N = int(input())
for i in range(N):
    B,C = input().split()
    B =int(B)
    for i in range(B-1):
        print(C[i],end="")
    for i in range(B,len(C)):
        print(C[i],end="")
    print("")