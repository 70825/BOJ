K=int(input())
D1,D2=map(int,input().split())
if D1==D2:print("{0:.2f}".format(K**2))
elif D1==3*D2:print("{0:.2f}".format(K**2-D2**2))
else:
    j=K**2-((D1-D2)/2)**2
    print("{0:.2f}".format(j))