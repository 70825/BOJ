D=[]
memo=[0 for i in range(100)]
for i in range(int(input())):
    a,b,c=map(int,input().split())
    D.append([c,a,b])
D.sort(reverse=True)
k=0;ans=0
while ans!=3:
    if memo[D[k][1]-1]!=2:
        print(D[k][1],D[k][2])
        memo[D[k][1]-1]+=1
        ans+=1
    k+=1