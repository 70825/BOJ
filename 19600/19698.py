D = list(map(int,input().split()))
x = (D[1]//D[3])*(D[2]//D[3])
if D[0] >= x: print(x)
else:print(D[0])