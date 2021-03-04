A = str(input())
C = [" ","0","1","2","3","4","5","6","7","8","9"]
for i in range(len(A)):
    if A[i] in C:
        print(A[i],end="")
    elif A[i] == A[i].lower():
        B = ord(A[i])
        if B >= 110:
            B = B-26
        print(chr(B+13),end="")
    elif A[i] == A[i].upper():
        B = ord(A[i])
        if B >= 78:
            B -= 26
        print(chr(B+13),end="")