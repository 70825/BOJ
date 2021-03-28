while 1:
    try:
        n, k = map(int,input().split())
        print(n + 1 + (n-k)//(k-1))
    except EOFError:
        break