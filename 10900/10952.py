while True:
    A,B = input().split()
    if 0< int(A) < 10 and 0 < int(B) < 10:
        print(int(A)+int(B))
    elif int(A) == 0 and int(B) == 0:
        break