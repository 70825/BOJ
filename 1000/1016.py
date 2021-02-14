Min,Max=map(int,input().split())
check=[True]*(Max-Min+1)
ans=Max-Min+1
n=1
while n*n<=Max:
    n+=1
    s=n*n
    i=Min//s
    while s*i<=Max:
        j = s*i-Min
        if j>=0 and check[j]:
            ans-=1
            check[j]=False
        i+=1
print(ans)