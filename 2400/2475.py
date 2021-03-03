A = input()
B = A.split(' ')
if len(B) == 5:
    a,b,c,d,e = A.split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    if 0<=a<=9 and 0<=b<=9 and 0<=c<=9 and 0<=d<=9 and 0<=e<=9:
        f = (a**2 + b**2 + c**2 + d**2 + e**2) % 10
        print(f)