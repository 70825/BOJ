while 1:
    try:A,B=map(float,input().split());print("{0:.2f}".format(A/B))
    except EOFError:break