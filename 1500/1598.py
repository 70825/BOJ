A,B = map(int,input().split())
if A % 4 == B % 4:
    print(abs(A//4-B//4))
elif A % 4 == 0:
    print(abs(4-B%4)+abs(A//4-1-B//4))
elif B % 4 == 0:
    print(abs(4-A%4)+abs(B//4-1-A//4))
else:
    print(abs(A%4-B%4)+abs(B//4-A//4))