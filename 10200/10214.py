T = int(input())
Yonsei = 0
Korea = 0
for j in range(T):
    for i in range(9):
        A = input()
        x, y = A.split(' ')
        if 0<= int(x) <=9 and 0<=int(y)<=9:
            if int(x) > int(y):
                Yonsei += 1
            elif int(x) < int(y):
                Korea += 1
    if Yonsei == Korea:
        print("Draw")
    elif Yonsei > Korea:
        print("Yonsei")
    elif Korea > Yonsei:
        print("Korea")