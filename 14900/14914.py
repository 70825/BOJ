A = input()
a,b = A.split()
a = int(a)
b = int(b)
if 1<=a<=1000 and 1<=b<=1000:
    c = min(a,b)
    for i in range(c):
        if a % (i+1) == 0 and b % (i+1) == 0:
            print(i+1,int(a/(i+1)),int(b/(i+1)))
        else:
            continue