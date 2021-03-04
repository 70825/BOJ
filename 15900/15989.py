def K(z):
    if i-z>=0:D[i]+=D[i-z]
D=[0]*(10001);D[0]=1
for k in range(3):
    for i in range(1,len(D)):K(k+1)
for i in range(int(input())):
    print(D[int(input())])