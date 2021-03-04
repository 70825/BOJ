for i in range(int(input())):
    b,p=map(float,input().split())
    print("{0:.4f}".format(60*(b-1)/p),"{0:.4f}".format(60*b/p),"{0:.4f}".format(60*(b+1)/p))