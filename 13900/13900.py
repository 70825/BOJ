N=int(input())
D=[*map(int,input().split())];ans=0
for i in range(N):ans+=D[i]**2
print((sum(D)**2-ans)//2)