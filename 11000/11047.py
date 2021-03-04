A,B = map(int,input().split())
C = [0] * 10
d = 0
for i in range(A):
    C[i] = int(input())
for i in range(A-1,-1,-1):
    while B >= C[i]:
        B -= C[i]
        d += 1
print(d)