T=123456*2
check=[0]*(T+1)
check[0]=check[1]=True
Prime=[]
for i in range(2,T+1):
    if not check[i]:
        Prime.append(i)
        j=2*i
        while j<=T:check[j]=True;j+=i
while 1:
    N=int(input())
    if N==0:break
    ans=0
    for i in Prime:
        if N<i<=2*N:ans+=1
        elif i>2*N:break
    print(ans)