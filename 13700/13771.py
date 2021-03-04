D=[]
for i in range(int(input())):
    D.append(float(input()))
D.sort()
print("{0:.2f}".format(D[1]))