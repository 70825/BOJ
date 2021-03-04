N=int(input())
D=[1];M=1
while M!=N+1:
    s=0
    for i in range(M):s+=D[i]*D[len(D)-1-i]
    M+=1
    D.append(s)
print(D[len(D)-1])