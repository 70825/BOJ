T = int(input())
a_cash = 0
b_cash = 0
if 1<= T <=1000:
    for i in range(T):
        A = input()
        a,b = A.split()
        a = int(a)
        b = int(b)
        if 0<=a<=100 and 0<=b<=64:
            if a == 0 or a >= 22:
                a_cash = 0
            elif a == 1:
                a_cash = 5000000
            elif a<=3:
                a_cash = 3000000
            elif a<=6:
                a_cash = 2000000
            elif a<=10:
                a_cash = 500000
            elif a<=15:
                a_cash = 300000
            elif a <=21:
                a_cash = 100000
            if b == 0 or b>=32:
                b_cash = 0
            elif b ==1:
                b_cash = 5120000
            elif b<=3:
                b_cash = 2560000
            elif b<=7:
                b_cash = 1280000
            elif b<=15:
                b_cash = 640000
            elif b<=31:
                b_cash = 320000
            print(a_cash + b_cash)