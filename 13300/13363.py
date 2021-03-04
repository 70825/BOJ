A=int(input())
B=int(input())
if A>B:
    if (360-A+B) <= A-B:print(360-A+B)
    else:print(B-A)
else:
    if (360-B+A)>=B-A:print(B-A)
    else:print(-(360-B+A))