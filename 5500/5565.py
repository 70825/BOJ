N = int(input())
B = [0] * 9
for i in range(9):
    A = int(input())
    if A<=10000:
        B[i] = A
print(N - sum(B))