def convert(n,base):
    T = "0123456789ABCDEF"
    q,r = divmod(n,base)
    if q == 0:
        return T[r]
    else:
        return convert(q,base)+T[r]
for i in range(1000,10000):
    d = i
    a = [0] * 3
    b = [0] * 3
    a[0] = convert(d,10)
    a[1] = convert(d,12)
    a[2] = convert(d,16)
    for j in range(3):
        for k in range(len(a[j])):
            if j == 0 :
                b[j] += int(a[j][k])
            else:
                if a[j][k] == "A":
                    b[j] += 10
                elif a[j][k] == "B":
                    b[j] += 11
                elif a[j][k] == "C":
                    b[j] += 12
                elif a[j][k] == "D":
                    b[j] += 13
                elif a[j][k] == "E":
                    b[j] += 14
                elif a[j][k] == "F":
                    b[j] += 15
                else:
                    b[j] += int(a[j][k])
    if b[0] == b[1] == b[2]:
        print(d)