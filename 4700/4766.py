K = []
C = float(input())
K.append(C)
i = 0
while True:
    A = float(input())
    K.append(A)
    if A == 999:
        break
    B = K[i+1]-K[i]
    print("{:.2f}".format(B))
    i += 1