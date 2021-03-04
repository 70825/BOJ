A = str(input())
if len(A) == 2:
    print(int(A[0]) + int(A[1]))
elif len(A) == 3:
    if A[1] == "0":
        print(10+int(A[2]))
    elif A[2] == "0":
        print(int(A[0])+10)
elif len(A) == 4:
    print("20")