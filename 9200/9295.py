T = int(input())
for i in range(T):
    K= input()
    x, y = K.split(' ')
    if 1<=int(x)<=6 and 1<=int(y)<=6:
        print("Case",str(i+1)+":",int(x)+int(y))
    else:
        break