T=1000000
Check=[0]*(T+1)
Check[0]=Check[1]=True
Prime=[]
for i in range(2,T+1):
    if not Check[i]:
        Prime.append(i)
        j = i+i
        while j<=T:
            Check[j]=True;j+=i
Prime.pop(0)
while 1:
    N=int(input())
    if N==0:break
    for i in Prime:
        if Check[N-i]==False:
            print("{} = {} + {}".format(N,i,N-i))
            break