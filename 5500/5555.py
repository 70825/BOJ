A = str(input())
N = int(input())
d = 0
for i in range(N):
    B = str(input())
    if A in B+B:
        d += 1
print(d)