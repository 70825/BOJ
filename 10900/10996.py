N = int(input())
if N == 1:
    print("*")
else:
    for i in range(2*N):
        for j in range(N):
            if i%2==0 and j%2==0:
                print("*",end="")
            elif i%2==0:
                print(" ",end="")
            elif i%2==1 and j%2==0:
                print(" ",end="")
            else:
                print("*",end="")
        print("")