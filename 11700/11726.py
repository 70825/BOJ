n=int(input())
D=[0]*1000;D[0]=1;D[1]=2
for i in range(2,n):D[i]=(D[i-1]+D[i-2])%10007
print(D[n-1])