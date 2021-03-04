N = int(input())
for i in range(N):
    A = str(input())
    if A[len(A)//2-1] == A[len(A)//2]:
        print("Do-it")
    else:
        print("Do-it-Not")