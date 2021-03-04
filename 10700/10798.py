A = ["A"] * 5
for i in range(5):
    A[i] = str(input())
for i in range(max(len(A[0]),len(A[1]),len(A[2]),len(A[3]),len(A[4]))):
    try:
        print(A[0][i],end="")
    except IndexError:
        print(end="")
    try:
        print(A[1][i],end="")
    except IndexError:
        print(end="")
    try:
        print(A[2][i],end="")
    except IndexError:
        print(end="")
    try:
        print(A[3][i],end="")
    except IndexError:
        print(end="")
    try:
        print(A[4][i],end="")
    except IndexError:
        print(end="")