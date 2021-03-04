T=int(input())
D=[1,1,1,2,2,3,4,5,7,9]
for i in range(10,100):
    D.append(D[i-1]+D[i-5])
for i in range(T):
    K=int(input())
    print(D[K-1])