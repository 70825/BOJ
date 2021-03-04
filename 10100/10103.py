T = int(input())
A = 100
B = 100
C = 0
if 1<= T <=15:
    for i in range(T):
        K= input()
        x, y = K.split(' ')
        if 1<=int(x)<=6 and 1<=int(y)<=6:
            C += 1
            if int(x) > int(y):
                B -= int(x)
            elif int(x) < int(y):
                A -= int(y)
        else:
            break
    if C == T:
        print(A)
        print(B)