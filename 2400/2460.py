A = 0
B = 0
for i in range(10):
    C,D = map(int,input().split())
    A += D-C
    if A > B:
        B = A
print(B)