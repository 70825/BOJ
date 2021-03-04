D=[]
for i in range(int(input())):
    D.append(int(input()))
D.sort();k=D[0]
for i in range(1,len(D)):
    k+=D[i];k/=2
print("{0:.6f}".format(k))