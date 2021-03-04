n=int(input())
D=[1]*1000
for i in range(1,n):
    if i%2==0:D[i]=D[i-1]*2-1
    else:D[i]=D[i-1]*2+1
    D[i]%=10007
print(D[n-1])