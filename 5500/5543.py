N = [0] * 3
C = [0] * 2
for i in range(3):
    N[i] = int(input())
for i in range(2):
    C[i] = int(input())
if min(N) >= 100 and max(N) <= 2000 and min(C) >= 100 and  max(N) <= 2000:
    F = min(N) + min(C) - 50
    print(F)