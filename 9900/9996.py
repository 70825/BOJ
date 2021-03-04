N = int(input())
B = input().split('*')
for i in range(N):
    A = input()
    d = 0
    if len(A) < len(B[0]) + len(B[1]):
        print("NE")
    else:
        for j in range(len(B[0])):
            if A[j] == B[0][j]:
                d += 1
        for j in range(len(B[1])):
            if A[len(A)-len(B[1])+j] == B[1][j]:
                d += 1
        if d == len(B[0])+len(B[1]) and len(A) >= (len(B[0])+len(B[1])):
            print("DA")
        else:
            print("NE")