A,B,C = input().split(' ')
A = int(A)
B = int(B)
C = int(C)
if min(A,B,C) >= 1 and  max(A,B,C) <= 10**12:
    print(A+B+C)