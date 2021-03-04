N,M=map(int,input().split())
D=[*map(int,input().split())]
ans=0
for i in range(1,N+1):
    for j in D:
    	if i%j==0:ans+=i;break
print(ans)