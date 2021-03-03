A = int(input())
B = int(input())
C = int(input())
k = [0] * 10
e = 0

if 100<= A < 1000 and 100<= B < 1000 and 100<= C < 1000:
    D = A * B * C
    while D > 0:
        D, e = divmod(D,10)
        for i in range(10):
            if i == e:
                k[i] += 1

for i in range(10):
    print(k[i])