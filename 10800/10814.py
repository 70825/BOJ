D=[[] for i in range(200)]
for i in range(int(input())):
    A,B=map(str,input().split())
    D[int(A)-1].append(B)
for i in range(200):
    if len(D)>0:
        for j in range(len(D[i])):
            print(i+1,D[i][j])