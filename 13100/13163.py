N = int(input())
if 1<=N<=100:
    for i in range(N):
        A = input()
        if len(A) <= 100:
            B = A.split()
            if len(B) >= 2:
                B[0]="god"
                for j in range(len(B)):
                    print(B[j],end="")
                print("")