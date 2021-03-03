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
Prime.append(1003001)
N=int(input())
for i in Prime:
    if i>=N:
        k=str(i);p=0
        for j in range(len(k)//2):
            if k[j]==k[len(k)-1-j]:p+=1
        if p==len(k)//2:
            print(k)
            break