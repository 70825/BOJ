while True:
    try:
        N,B,M=map(float,input().split());year=0
        while N<=M:N+=N*B/100;year+=1
        print(year)
    except EOFError:break