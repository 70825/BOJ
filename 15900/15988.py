D=[0,1,2,4]
D[1],D[2],D[3]=1,2,4
for i in range(4,1000001):
    D.append((D[i-1]+D[i-2]+D[i-3])%((10**9)+9))
for _ in range(int(input())):
    print(D[int(input())])