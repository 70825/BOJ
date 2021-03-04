N=int(input())
D=[0]+[*map(int,input().split())]
d=[-1]*(N+1);d[0]=0
for i in range(1,N+1):
    for j in range(1,i+1):
        if d[i]==-1 or d[i]>d[i-j]+D[j]:
            d[i]=d[i-j]+D[j]
print(d[N])