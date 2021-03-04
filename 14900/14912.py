A = input()
N, d = A.split()
if 1<=int(N)<=100000 and 0<=int(d)<=9:
    c = 0
    B = int(N)
    C = B
    D = str(C)
    for i in range(B):
        for j in range(len(str(C))):
            if D[j] == d:
                c += 1
        C -= 1
        D = str(C)
    print(c)