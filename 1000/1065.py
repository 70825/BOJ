a = int(input())
if a < 100 and a >= 1:
    print(a)
elif a >= 100  and a <= 1000:
    t = 99
    for i in range(100,int(a+1)):
        B = i
        b,B = divmod(B,100)
        c,d = divmod(B, 10)
        if b - c == c - d:
            t += 1
    print(t)