for i in range(int(input())):
    a=input();b=a[::-1];c=str(int(a)+int(b))
    if c==c[::-1]:print('YES')
    else:print('NO')