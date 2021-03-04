A = input()
B = A.split()
a = 0
if len(B) <= 1000000:
    for i in range(len(B)):
        if int(B[i]) < -1000000 or int(B[i]) > 1000000:
            break
        elif int(B[i]) > 0:
            a += 1
    print(a)