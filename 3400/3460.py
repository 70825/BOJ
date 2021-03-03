T = int(input())
for i in range(T):
    A = int(input())
    B = str(bin(A))
    c = []
    for j in range(len(B)):
        if B[j] == "1":
            c.append(len(B)-1-j)
    c.sort()
    for j in range(len(c)):
        print(c[j],end=" ")