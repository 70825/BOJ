for i in range(int(input())):
    N=[*map(str,input().split())]
    for j in range(len(N)):
        print(N[j][::-1],end=" ")
    print("")