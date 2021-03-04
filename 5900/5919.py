N=int(input())
D=[0]*N
move=0
for i in range(N):
    D[i]=int(input())
k=sum(D)//N
for i in range(N):
    if k>D[i]:
        move+=k-D[i]
print(move)