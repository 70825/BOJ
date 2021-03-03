B = 0
C = 100
for i in range(7):
    A = int(input())
    if A % 2 == 1:
        B += A
        if A < C:
            C = A
if B == 0:
    print("-1")
else:
    print(B)
    print(C)