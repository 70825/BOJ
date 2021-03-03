A = [0] * 4
B = 0
for i in range(4):
    C,D = map(int,input().split())
    B += D-C
    A[i] = B
print(max(A))